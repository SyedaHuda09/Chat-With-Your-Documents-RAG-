from pathlib import Path
import pytest
from ingestion import load_pdfs

def test_load_pdfs_rejects_missing_file():
    with pytest.raises(FileNotFoundError):
        load_pdfs(["does-not-exist.pdf"])

def test_load_pdfs_rejects_non_pdf(tmp_path: Path):
    p = tmp_path / "document.txt"
    p.write_text("not a PDF", encoding="utf-8")
    with pytest.raises(ValueError):
        load_pdfs([str(p)])
