import streamlit as st
import ollama
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from docx import Document
import re
from pydantic import BaseModel

st.set_page_config(page_title="AI Finance Assistant", layout="wide")

# ---------------- PYDANTIC ---------------- #
class AIResponse(BaseModel):
    answer: str
    source: str

# ---------------- EMBEDDING ---------------- #
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

embed_model = load_model()

# ---------------- SESSION ---------------- #
if "index" not in st.session_state:
    st.session_state.index = faiss.IndexFlatL2(384)
    st.session_state.docs = []
    st.session_state.full_doc = ""

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- FILE ---------------- #
def read_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text.strip() for p in doc.paragraphs if p.text.strip()])
    return ""

# ---------------- SMART CHUNK ---------------- #
def chunk_text(text, size=700, overlap=100):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += size - overlap
    return chunks

# ---------------- EMBED ---------------- #
def embed_document(text):
    chunks = chunk_text(text)
    emb = embed_model.encode(chunks, convert_to_numpy=True)

    st.session_state.index.reset()
    st.session_state.index.add(np.array(emb).astype("float32"))
    st.session_state.docs = chunks
    st.session_state.full_doc = text

# ---------------- RETRIEVE ---------------- #
def retrieve(query, k=6):
    if not st.session_state.docs:
        return ""

    q_vec = embed_model.encode([query], convert_to_numpy=True)
    _, I = st.session_state.index.search(np.array(q_vec).astype("float32"), k)

    return "\n\n".join([st.session_state.docs[i] for i in I[0]])

# ---------------- QUESTION ---------------- #
def extract_question(query, text):
    match = re.search(r"(q|question)\s*(\d+)", query.lower())
    if not match:
        return None

    num = match.group(2)
    pattern = rf"{num}\.\s*(.+?)(?=\n\d+\.|\Z)"
    result = re.findall(pattern, text, re.DOTALL)

    return result[0].strip() if result else None

def extract_all_questions(text):
    return re.findall(r"\d+\.\s.*", text)

# ---------------- CHAT MODE ---------------- #
def is_casual_chat(text):
    text = text.lower()
    return any(x in text for x in ["hi","hello","thanks","thank","ok","bye"])

def casual_response(text):
    text = text.lower()
    if "thank" in text:
        return "You're welcome 😊"
    if "hi" in text:
        return "Hi! How can I help you today?"
    if "bye" in text:
        return "Goodbye! 👋"
    if "ok" in text:
        return "Got it 👍"
    return "😊"

# ---------------- INVALID ---------------- #
def is_invalid(text):
    return len(text.strip()) < 3 or not any(c.isalpha() for c in text)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.title("⚙ Controls")

    file = st.file_uploader("Upload (.txt / .docx)")

    if file:
        text = read_file(file)
        if text:
            embed_document(text)
            st.success("✅ Document embedded!")

    if st.button("🗑 Clear Chat"):
        st.session_state.chat = []
        st.rerun()

# ---------------- UI ---------------- #
st.title("💰 AI Finance Assistant")

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")

# ---------------- INPUT ---------------- #
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask anything...", label_visibility="collapsed")
    send = st.form_submit_button("Send")

# ---------------- MAIN ---------------- #
if send and user_input:

    st.session_state.chat.append(("user", user_input))

    # ❌ Invalid
    if is_invalid(user_input):
        st.session_state.chat.append(("bot", "⚠️ Invalid query"))
        st.rerun()

    # ✅ Casual chat
    if is_casual_chat(user_input):
        st.session_state.chat.append(("bot", casual_response(user_input)))
        st.rerun()

    full_doc = st.session_state.full_doc

    # 🔥 USE FULL DOC IF SMALL (VERY IMPORTANT)
    if len(full_doc) < 3000 and full_doc:
        context = full_doc
    else:
        context = retrieve(user_input)

    # 🎯 CASES
    if "all questions" in user_input.lower() and full_doc:
        questions = extract_all_questions(full_doc)

        prompt = f"""
Answer ALL questions clearly:

{chr(10).join(questions)}
"""
        source = "document"

    else:
        q = extract_question(user_input, full_doc)

        if q:
            prompt = f"""
Use this document context to answer fully:

{context}

Question:
{q}
"""
            source = "document"

        elif context:
            prompt = f"""
Answer using context:

{context}

User:
{user_input}
"""
            source = "document"

        else:
            prompt = user_input
            source = "general"

    # 🔥 THINKING UI
    placeholder = st.empty()
    placeholder.markdown("**🤖 Thinking...**")

    try:
        response = ollama.chat(
            model="phi",  # 🔥 BEST: phi3:mini
            messages=[{"role": "user", "content": prompt}],
            options={
                "num_predict": 100,
                "temperature": 0.3,
                "top_k": 10
            }
        )

        reply = response["message"]["content"]

        placeholder.markdown(f"**🤖 AI:** {reply}")

    except Exception as e:
        reply = f"⚠️ Error: {e}"
        placeholder.markdown(f"**🤖 AI:** {reply}")

    # ---------------- PYDANTIC ---------------- #
    try:
        structured = AIResponse(answer=reply.strip(), source=source)
        final = f"{structured.answer}\n\n📌 Source: {structured.source}"
    except:
        final = reply

    st.session_state.chat.append(("bot", final))
    st.rerun()
    