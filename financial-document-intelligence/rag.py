from pathlib import Path
from typing import Sequence
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import settings

INDEX_DIR = Path(".faiss_index")

def build_vector_store(chunks: Sequence[Document]) -> FAISS:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not configured.")
    return FAISS.from_documents(list(chunks), OpenAIEmbeddings(model=settings.embedding_model))

def answer_question(store: FAISS, question: str, top_k: int | None = None):
    docs = store.as_retriever(search_kwargs={"k": top_k or settings.top_k}).invoke(question)
    context = "\n\n".join(
        f"[Source: {d.metadata.get('source_file','unknown')}, page {d.metadata.get('page_number','?')}]\n{d.page_content}"
        for d in docs
    )
    prompt = f"""You are a financial document assistant.
Use ONLY the supplied document context. If evidence is insufficient, say so.
Do not invent financial figures.

Context:
{context}

Question:
{question}

Give a concise grounded answer and cite source file/page numbers."""
    llm = ChatOpenAI(model=settings.chat_model, temperature=0, api_key=settings.openai_api_key)
    return llm.invoke(prompt).content, docs
