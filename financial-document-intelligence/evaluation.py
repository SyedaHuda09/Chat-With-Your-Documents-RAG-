"""Lightweight RAG evaluation helpers."""

from dataclasses import dataclass

@dataclass
class EvaluationResult:
    question: str
    answer: str
    retrieved_documents: int
    has_source_reference: bool

def evaluate_response(question: str, answer: str, documents: list) -> EvaluationResult:
    markers = ("page", "source", ".pdf")
    return EvaluationResult(
        question=question,
        answer=answer,
        retrieved_documents=len(documents),
        has_source_reference=any(m in answer.lower() for m in markers),
    )
