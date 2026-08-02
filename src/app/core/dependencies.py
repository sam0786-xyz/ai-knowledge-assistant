from pathlib import Path

from app.services.document_service import DocumentService
from app.storage import LocalStorage


def get_storage() -> LocalStorage:
    return LocalStorage(
        upload_dir=Path("uploads"),
    )


def get_document_service() -> DocumentService:
    storage = get_storage()
    return DocumentService(storage=storage)
