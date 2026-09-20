"""Production vector-store boundary for Amazon OpenSearch Service."""

from dataclasses import dataclass
from typing import Any

@dataclass
class OpenSearchConfig:
    endpoint: str
    index_name: str
    region: str = "eu-central-1"

class OpenSearchVectorStore:
    def __init__(self, config: OpenSearchConfig):
        self.config = config

    def similarity_search(self, query: str, k: int = 4) -> list[dict[str, Any]]:
        raise NotImplementedError(
            "Implement this adapter with an authenticated OpenSearch client for cloud deployment."
        )
