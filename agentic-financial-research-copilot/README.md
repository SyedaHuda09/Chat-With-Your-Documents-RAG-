# Agentic Financial Research Copilot

A production-oriented AI agent that combines **RAG, tool calling, financial calculations, source attribution, and evaluation** into one workflow.

## What it demonstrates

- Agentic routing: decide whether a question needs retrieval, calculation, or both
- Retrieval over financial-document chunks
- OpenAI tool/function calling
- Deterministic financial calculator tool
- Grounded answers with source/page references
- FastAPI service endpoint
- Offline retrieval fallback for local development
- Evaluation harness for answer faithfulness and citation coverage
- Clear separation between model, tools, retrieval, and API layers

## Architecture

User question
→ Agent router
→ {Retriever | Calculator | Retriever + Calculator}
→ Context + tool results
→ LLM synthesis
→ Answer + citations

## Example questions

- "What was the company's revenue in 2024?"
- "What is the year-over-year revenue growth from 2023 to 2024?"
- "Which document/page supports the operating margin figure?"
- "Compare revenue and operating income across two reporting periods."

## Run locally

```bash
cd agentic-financial-research-copilot
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Add OPENAI_API_KEY if you want LLM synthesis.

uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## API

POST `/ask`

```json
{
  "question": "What was revenue growth from 2023 to 2024?"
}
```

## Production evolution

This project is intentionally designed as an extensible architecture. The local lexical retriever can be replaced by FAISS/OpenSearch, the document loader can be connected to S3/Textract, and tracing/evaluation can be connected to LangSmith without changing the agent/tool interfaces.
