AI_LOG.md
Project: AI Finance Assistant (RAG-based Chatbot using Ollama + FAISS + Streamlit)
📅 April 24, 2026
Prompt 1
What I asked:
"Build a Streamlit chatbot using Ollama phi model."
What AI gave:
A basic chatbot with input box, response display, and Ollama integration for generating replies.
What I kept:
Streamlit UI structure
Ollama integration for local LLM
What I rejected:
Basic response logic because it was not using any document context
Reason:
The project required document-based answering, not just general responses.
Prompt 2
What I asked:
"Improve UI and make it professional with dark and light mode."
What AI gave:
A styled UI with colors, chat bubbles, and layout suggestions.
What I kept:
Clean layout
Dark theme base
Chat bubble structure
What I rejected:
Bright or colorful UI styles
Reason:
Needed a professional minimal UI, not a colorful or childish design.
Issues Faced
Chatbot worked but gave only general answers
No document understanding


📅 April 25, 2026
Prompt 3
What I asked:
"Add document upload and retrieval using embeddings and FAISS."
What AI gave:
Code for:
Sentence-transformers embeddings
FAISS vector storage
Document chunking
What I kept:
FAISS indexing
Embedding model (MiniLM)
Document upload logic
What I rejected:
Very small chunk size
Reason:
Small chunks caused incomplete answers
Prompt 4
What I asked:
"Fix chatbot saying 'not found in document' even when answer exists."
What AI gave:
Suggestions:
Increase chunk size
Increase top-k retrieval
Improve prompt
What I kept:
Larger chunk size + overlap
Increased retrieval results
What I rejected:
Complex multi-step retrieval pipelines
Reason:
Wanted simple + fast system
Prompt 5
What I asked:
"Fix question number detection (like Q1, Q7)."
What AI gave:
Regex-based extraction logic.
What I kept:
Regex for extracting numbered questions
What I rejected:
Simple line matching
Reason:
It returned wrong question answers
Issues Faced
Wrong answers for question numbers
Partial answers from document
Slow response


📅 April 26, 2026
Prompt 6
What I asked:
"Improve speed and make chatbot fast using phi."
What AI gave:
Suggestions:
Reduce tokens
Optimize prompt
Use streaming
What I kept:
Reduced token size
Optimized prompt
What I rejected:
Too low token limit
Reason:
It caused incomplete answers
Prompt 7
What I asked:
"Make chatbot behave like ChatGPT (conversation style)."
What AI gave:
Casual chat detection (hi, thanks, etc.)
What I kept:
Conversation handling logic
What I rejected:
Using document for all responses
Reason:
Casual chat should feel natural, not document-based
Prompt 8
What I asked:
"Add structured output using Pydantic."
What AI gave:
Pydantic model with JSON structure.
What I kept:
Pydantic class for response validation
What I rejected:
Strict JSON enforcement
Reason:
Phi model sometimes returns invalid JSON
Additional Improvements
Added “Thinking…” indicator
Added invalid input detection
Improved full document usage for better answers
⚠️ Bug Introduced by AI
AI suggested small chunk size, which caused loss of context.
How I identified:
Wrong answers for document questions.


Fix:
Increased chunk size and overlap.
🎯 Design Decision Against AI
AI suggested adding complex pipelines and extra features.
Decision:
Used simple FAISS + direct retrieval.
Reason:
To maintain speed and simplicity
⏱️ Time Distribution
Writing code: 40%
Prompting AI: 20%
Reviewing AI output: 15%
Debugging: 15%
Testing: 5%
Reading docs: 5%

