from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Financial Document Intelligence API", version="1.0.0")

class QuestionRequest(BaseModel):
    question: str
    top_k: int = 4

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(request: QuestionRequest):
    return {
        "status": "service-boundary-ready",
        "message": "Connect this endpoint to a persistent vector store for deployment.",
        "question": request.question,
        "top_k": request.top_k,
    }
