# Financial Document Intelligence RAG

A production-oriented Retrieval-Augmented Generation (RAG) system for asking grounded questions over financial documents.

## What this demonstrates

- PDF ingestion and page-level metadata
- Recursive chunking
- OpenAI embeddings
- FAISS retrieval for lightweight local development
- Grounded LLM generation with source/page attribution
- Streamlit UI
- FastAPI service boundary
- AWS Textract adapter for scanned/complex documents
- OpenSearch adapter boundary for scalable vector search
- Lightweight RAG evaluation hooks
- Environment-based configuration
- Security-conscious secret handling
- Migration path from local prototype to cloud architecture

## Architecture

```
Financial PDFs
   |
   v
PDF / AWS Textract extraction
   |
   v
Chunking + page metadata
   |
   v
OpenAI embeddings
   |
   +--> FAISS (local)
   |
   +--> OpenSearch (production adapter)
   |
   v
Top-k evidence
   |
   v
LLM grounded prompt
   |
   v
Answer + source/page citations
```

## Local development

FAISS keeps the project lightweight enough for normal laptop development.

```bash
cd financial-document-intelligence
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

API:

```bash
uvicorn api:app --reload
```

## Production direction

- **S3** for durable document storage
- **AWS Textract** for scanned/complex documents
- **OpenSearch** for scalable vector retrieval
- **FastAPI** for service/API access
- **AKS or another container platform** for deployment
- **LangSmith** for tracing/observability
- **Evaluation harness** for retrieval and answer quality
- **Human-in-the-loop** review for sensitive financial workflows

The AWS and OpenSearch integrations are deliberately explicit adapters/boundaries; this repository does not claim that those cloud services are already deployed.

## Evaluation

`evaluation.py` provides a lightweight structure for checking whether generated responses contain source references. It can be expanded with retrieval precision/recall, faithfulness, context relevance, citation correctness, latency, and cost metrics.

## Security

Never commit `.env`, API keys, private financial documents, customer data, or generated vector indexes containing sensitive information. Use IAM roles/managed identities rather than hard-coded cloud credentials.

## Portfolio talking points

- FAISS versus managed OpenSearch trade-offs
- PDF extraction versus Textract
- Chunk size/top-k retrieval tuning
- Grounding and citation requirements
- Observability and evaluation
- Separating the RAG engine from the UI/API
