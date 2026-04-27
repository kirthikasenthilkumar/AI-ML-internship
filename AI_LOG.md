# 📄 AI_LOG.md

## Project: AI Finance Assistant (RAG-based Chatbot using Ollama + FAISS + Streamlit)

---

## 📅 April 24, 2026

### 🔹 Prompt 1

**What I asked:**
"Build a Streamlit chatbot using Ollama phi model."

**What AI gave:**

* Basic chatbot
* Input box
* Response display
* Ollama integration for replies

**What I kept:**

* Streamlit UI structure
* Ollama integration for local LLM

**What I rejected:**

* Basic response logic (no document context)

**Reason:**
The project required document-based answering, not general responses.

---

### 🔹 Prompt 2

**What I asked:**
"Improve UI and make it professional with dark and light mode."

**What AI gave:**

* Styled UI
* Colors and chat bubbles
* Layout suggestions

**What I kept:**

* Clean layout
* Dark theme base
* Chat bubble structure

**What I rejected:**

* Bright/colorful UI styles

**Reason:**
Needed a professional, minimal UI—not a colorful or childish design.

---

### ⚠️ Issues Faced

* Chatbot gave only general answers
* No document understanding

---

## 📅 April 25, 2026

### 🔹 Prompt 3

**What I asked:**
"Add document upload and retrieval using embeddings and FAISS."

**What AI gave:**

* Sentence-transformers embeddings
* FAISS vector storage
* Document chunking

**What I kept:**

* FAISS indexing
* Embedding model (MiniLM)
* Document upload logic

**What I rejected:**

* Very small chunk size

**Reason:**
Small chunks caused incomplete answers.

---

### 🔹 Prompt 4

**What I asked:**
"Fix chatbot saying 'not found in document' even when answer exists."

**What AI gave:**

* Increase chunk size
* Increase top-k retrieval
* Improve prompt

**What I kept:**

* Larger chunk size with overlap
* Increased retrieval results

**What I rejected:**

* Complex multi-step retrieval pipelines

**Reason:**
Wanted a simple and fast system.

---

### 🔹 Prompt 5

**What I asked:**
"Fix question number detection (like Q1, Q7)."

**What AI gave:**

* Regex-based extraction logic

**What I kept:**

* Regex for extracting numbered questions

**What I rejected:**

* Simple line matching

**Reason:**
It returned incorrect answers.

---

### ⚠️ Issues Faced

* Wrong answers for question numbers
* Partial answers from documents
* Slow response

---

## 📅 April 26, 2026

### 🔹 Prompt 6

**What I asked:**
"Improve speed and make chatbot fast using phi."

**What AI gave:**

* Reduce tokens
* Optimize prompt
* Use streaming

**What I kept:**

* Reduced token size
* Optimized prompt

**What I rejected:**

* Too low token limit

**Reason:**
Caused incomplete answers.

---

### 🔹 Prompt 7

**What I asked:**
"Make chatbot behave like ChatGPT (conversation style)."

**What AI gave:**

* Casual chat detection (hi, thanks, etc.)

**What I kept:**

* Conversation handling logic

**What I rejected:**

* Using document for all responses

**Reason:**
Casual chat should feel natural, not document-based.

---

### 🔹 Prompt 8

**What I asked:**
"Add structured output using Pydantic."

**What AI gave:**

* Pydantic model with JSON structure

**What I kept:**

* Pydantic class for response validation

**What I rejected:**

* Strict JSON enforcement

**Reason:**
Phi model sometimes returns invalid JSON.

---

## 🚀 Additional Improvements

* Added **“Thinking…” indicator**
* Added **invalid input detection**
* Improved **full document usage** for better answers

---

## ⚠️ Bug Introduced by AI

**Issue:**
AI suggested small chunk size → caused loss of context

**How I identified:**
Wrong answers for document-based questions

**Fix:**
Increased chunk size and added overlap

---

## 🎯 Design Decision Against AI

**AI Suggestion:**
Use complex pipelines and extra features

**Decision:**
Used simple FAISS + direct retrieval

**Reason:**
Maintains speed and simplicity

---

## ⏱️ Time Distribution

* Writing code: **40%**
* Prompting AI: **20%**
* Reviewing AI output: **15%**
* Debugging: **15%**
* Testing: **5%**
* Reading docs: **5%**

---

✨ **Final Note:**
Focused on building a **fast, simple, and document-aware chatbot** rather than a complex system.

