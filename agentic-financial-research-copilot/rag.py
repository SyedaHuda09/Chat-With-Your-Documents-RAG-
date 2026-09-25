"""Small dependency-light retriever for demonstrating the RAG boundary.

Replace this implementation with FAISS/OpenSearch in production.
"""

from dataclasses import dataclass
import re
from typing import Iterable


@dataclass
class Chunk:
    text: str
    source: str
    page: int


DEFAULT_CHUNKS = [
    Chunk(
        "Revenue was $12.4 billion in 2024, compared with $10.0 billion in 2023.",
        "annual_report_2024.pdf",
        42,
    ),
    Chunk(
        "Operating income was $2.1 billion in 2024 and $1.6 billion in 2023.",
        "annual_report_2024.pdf",
        44,
    ),
    Chunk(
        "The company reported an operating margin of 16.9% in 2024 versus 16.0% in 2023.",
        "annual_report_2024.pdf",
        45,
    ),
]


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


class LocalRetriever:
    def __init__(self, chunks: Iterable[Chunk] = DEFAULT_CHUNKS):
        self.chunks = list(chunks)

    def search(self, query: str, k: int = 4) -> list[Chunk]:
        q = _tokens(query)
        ranked = sorted(
            self.chunks,
            key=lambda c: len(q & _tokens(c.text)),
            reverse=True,
        )
        return ranked[:k]
