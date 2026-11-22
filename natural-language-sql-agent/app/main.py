from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .agent import answer_question
from .security import UnsafeQueryError

app = FastAPI(
    title="Natural Language SQL Agent",
    description="Generate and execute validated read-only SQL from natural-language questions.",
    version="1.0.0",
)


class QueryRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query")
def query_database(request: QueryRequest):
    try:
        return answer_question(request.question)
    except UnsafeQueryError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        # Avoid exposing provider or database internals to API clients.
        raise HTTPException(status_code=500, detail="Unable to process the query.") from exc
