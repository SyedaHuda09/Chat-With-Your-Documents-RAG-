"""AWS Textract integration boundary for scanned/complex documents."""

from dataclasses import dataclass

@dataclass
class TextractConfig:
    region: str = "eu-central-1"

class TextractDocumentExtractor:
    def __init__(self, config: TextractConfig | None = None):
        self.config = config or TextractConfig()

    def start_s3_text_detection(self, bucket: str, key: str) -> str:
        import boto3
        client = boto3.client("textract", region_name=self.config.region)
        response = client.start_document_text_detection(
            DocumentLocation={"S3Object": {"Bucket": bucket, "Name": key}}
        )
        return response["JobId"]
