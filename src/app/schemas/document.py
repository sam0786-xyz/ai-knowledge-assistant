from uuid import UUID
from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    """Response returned after a document is successfully uploaded."""

    document_id: UUID
    filename: str
    status: str
