from fastapi import FastAPI
from app.api import documents, health

from app.core.config import settings

app = FastAPI(title=settings.app_name, version=settings.app_version)

app.include_router(health.router)
app.include_router(documents.router, prefix="/documents", tags=["Documents"])
