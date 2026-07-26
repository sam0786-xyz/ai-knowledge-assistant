from uuid import uuid4
from pathlib import Path

from app.storage.local_storage import LocalStorage
from app.schemas.document import DocumentUploadResponse


class DocumentService:
    def __init__(self, storage: LocalStorage):
        self.storage = storage

    def upload(self, filename: str, content: bytes) -> DocumentUploadResponse:
        """Uploads a document to the local storage."""
        original_path = Path(filename)
        extension = original_path.suffix
        document_id = uuid4()
        storage_filename = f"{document_id}{extension}"
        self.storage.save(storage_filename, content)
        return DocumentUploadResponse(
            document_id=document_id, filename=filename, status="uploaded"
        )
