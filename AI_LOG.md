
Tools used
ChatGPT – used for debugging RAG issues, improving retrieval logic, optimizing speed, and designing prompts
GitHub Copilot – used for code completion, minor fixes, and speeding up development in VS Code


Significant prompts
1. Prompt:
"Build a Streamlit AI chatbot using Ollama (phi model) with document upload and answering capability."
What AI produced:
A basic chatbot with Ollama integration and simple input/output handling.
What I kept / rejected and why:
Kept the basic chatbot structure and Ollama integration because it worked locally without API keys.
Rejected the simple response logic because it did not support document-based answers.
2. Prompt:
"Add document retrieval using embeddings and FAISS."
What AI produced:
Code for embedding documents using sentence-transformers and storing vectors in FAISS.
What I kept / rejected and why:
Kept FAISS indexing and embedding logic because it enabled document search.
Rejected small chunk sizes because they caused incomplete answers and poor retrieval accuracy.
3. Prompt:
"Fix issue where chatbot says 'not found in document' even when answer exists."
What AI produced:
Suggestions to improve chunking, retrieval count, and prompt design.
What I kept / rejected and why:
Kept larger chunk size and increased top-k retrieval because it improved accuracy.
Rejected overly complex retrieval pipelines to keep performance fast.
4. Prompt:
"Make chatbot responses faster using phi model."
What AI produced:
Optimization suggestions like reducing tokens, adjusting temperature, and simplifying prompts.
What I kept / rejected and why:
Kept lower token generation and simplified prompts for faster response.
Rejected very low token limits because they caused incomplete answers.


5. Prompt:
"Add structured output using Pydantic."
What AI produced:
Code using Pydantic models to structure responses.
What I kept / rejected and why:
Kept Pydantic model for validation.
Modified implementation to avoid strict JSON failures with phi model.


6. Prompt:
"Make chatbot behave like ChatGPT (conversation style)."
What AI produced:
Logic to detect casual chat (hi, thanks, etc.) and respond naturally.
What I kept / rejected and why:
Kept conversational intent detection because it improved user experience.
Rejected forcing all responses through document retrieval.


7. Prompt:
"Fix question number extraction (Q1, Q7 issue)."


What AI produced:
Regex-based extraction logic.
What I kept / rejected and why:
Kept improved regex for multi-line question extraction.
Rejected simple line-based matching because it returned wrong answers.
A bug your AI introduced
AI initially suggested very small chunk sizes for document embedding.


Issue:
Important information was split across chunks, causing incorrect or incomplete answers.
How I caught it:
When asking “Answer question 1”, the chatbot returned unrelated or partial answers.


Fix:
Increased chunk size and overlap to ensure full context is retrieved.
A design choice you made against AI suggestion
AI suggested using complex pipelines and multiple retrieval steps.
I simplified the system to:
Single FAISS index
Direct retrieval + prompt injection
Why:
To maintain faster response time and avoid unnecessary complexity for a local project.


Time split
Writing code: 40%
Prompting AI tools: 20%
Reviewing AI output: 15%
Debugging: 15%
Testing: 5%
Reading documentation: 5%
