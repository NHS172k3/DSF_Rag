RAG based chatbot trained on DSF documents for quiz prep purposes
# DSF_Rag

## Overview
DSF_Rag is a Retrieval-Augmented Generation (RAG) based chatbot designed to assist with quiz preparation using SC3021 course documents. It indexes course materials and provides context-aware answers to user queries.

## Tech Stack
- Streamlit (web UI)
- LlamaIndex (RAG pipeline, document parsing)
- Supabase (vector store backend)
- HuggingFace Transformers & Embeddings
- Groq API (Llama 70B model)


## Features
- Ingests and parses SC3021 course documents (Markdown, text)
- Builds vector and document stores for efficient retrieval
- RAG-based chatbot for interactive Q&A
- Useful for quiz and exam preparation

## Project Structure

- `app/` – Main application code
  - `app.py` – Entry point for the chatbot web app
  - `utils.py` – Utility functions for parsing and retrieval
  - `requirements.txt` – Python dependencies
- `data/` – Notebooks and data files
- `index_store/` – Generated index and vector store files
- `parsed/` – Parsed course documents (Markdown, text)
- `prompts/` – Prompt templates for the chatbot
- `docparser.py` – Script for parsing and indexing documents
- `index.py` – Script for building and updating the index

## Setup
1. Clone the repository and navigate to the project directory.
2. Create and activate a Python virtual environment:
	```
	python -m venv .venv
	.venv\Scripts\activate  # On Windows
	```
3. Install dependencies:
	```
	pip install -r app/requirements.txt
	```

## Usage
1. Parse and index documents (if not already done):
	```
	python docparser.py
	python index.py
	```
2. Start the chatbot application:
	```
	python app/app.py
	```
3. Interact with the chatbot via the provided interface.

## Notes
- Ensure all DSF course documents are placed in the `parsed/` directory before indexing.
- The chatbot uses the generated index and vector stores in `index_store/` for retrieval.

## License
This project is for educational use only.
