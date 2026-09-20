# Financial Document Intelligence RAG

A production-oriented RAG application for asking grounded questions over financial PDFs.

## Architecture

PDFs → extraction → chunking + metadata → embeddings → FAISS retrieval → LLM → grounded answer + source/page citations

## Features

- Financial PDF ingestion with page metadata
- Recursive chunking
- OpenAI embeddings
- Local FAISS vector retrieval
- Configurable top-k retrieval
- Grounded answers with source/page references
- Streamlit interface
- OpenSearch adapter boundary for production scaling
- Environment-based configuration
- Basic ingestion tests

## Project structure

```
financial-document-intelligence/
├── app.py
├── config.py
├── ingestion.py
├── rag.py
├── opensearch_store.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── tests/
    └── test_ingestion.py
```

## Run

```bash
cd financial-document-intelligence
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

Add your OpenAI API key to `.env`. The local FAISS workflow does not require a separate vector database.

## Production architecture

The project is structured so the local FAISS implementation can evolve toward:

- AWS S3 for document storage
- AWS Textract for document extraction
- Amazon OpenSearch Service for scalable vector retrieval
- AKS/container deployment
- LangSmith tracing and observability
- Retrieval and generation evaluation
- Human-in-the-loop review for sensitive financial workflows

## Security

Never commit `.env`, API keys, private financial documents, or generated vector indexes containing sensitive data.

## Portfolio context

This project demonstrates practical RAG engineering across ingestion, chunking, embeddings, vector retrieval, grounded generation, source attribution, application UI, testing, and a production-oriented OpenSearch migration boundary.
