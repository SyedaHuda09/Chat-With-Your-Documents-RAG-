# DocuMind — Chat With Your Documents (RAG)

Ask natural-language questions over a set of PDFs and get grounded answers with source citations, 
built with LangChain, OpenAI/Hugging Face embeddings, and FAISS.

## Why I built this
[1-2 sentences: e.g. "To apply production RAG patterns I used professionally at PixelEdge Solutions 
in a fully open, demonstrable project."]

## Demo
🔗 [Live demo on Hugging Face Spaces](link)
![demo](docs/demo.gif)

## Architecture
User question → retriever (FAISS, top-k) → LLM (OpenAI/HF) grounded in retrieved chunks → answer + source

## Tech stack
Python · LangChain · OpenAI/Hugging Face · FAISS · Streamlit · PyTest

## Setup
```bash
git clone ...
pip install -r requirements.txt
streamlit run app.py
```

## What I'd improve next
- [ ] Add re-ranking for better retrieval precision
- [ ] Swap FAISS for OpenSearch for scale
- [ ] Add evaluation harness (faithfulness / relevance scoring)
