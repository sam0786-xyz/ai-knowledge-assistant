from fastapi import APIRouter, Depends, File, UploadFile
from typing import Annotated
from fastapi import HTTPException

from app.core.dependencies import get_document_service
from app.schemas.document import DocumentUploadResponse
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
)
async def upload(
    file: Annotated[UploadFile, File()],
    service: Annotated[
        DocumentService,
        Depends(get_document_service),
    ],
) -> DocumentUploadResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    filename = file.filename
    content = await file.read()

    response = service.upload(
        filename=filename,
        content=content,
    )

    return response
