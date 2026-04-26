# AI Finance Assistant

A Streamlit-based finance assistant that uses Ollama's `phi` model to answer finance questions and provide document-aware responses.

## Features
- Upload `.txt` or `.docx` documents
- Extract and embed document content
- Search relevant sections using semantic retrieval
- Answer finance questions using document context or general finance knowledge
- Structured output with answer, source, and confidence

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```
3. Upload a document and ask finance questions in the chat.

## Notes
- The app uses the `phi` model from Ollama
- Document extraction supports plain text and `.docx` tables
- The repository contains `app.py`, `requirements.txt`, and `.gitignore`
