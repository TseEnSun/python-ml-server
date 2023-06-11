from fastapi import FastAPI
from app.config import settings
from app.api.api_v1.api import api_router
from app.api.endpoints import health_check

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_PATH}/openapi.json",
    docs_url=f"{settings.API_PATH}/docs",
)

app.include_router(health_check.router, prefix=settings.API_PATH)
app.include_router(api_router, prefix=settings.API_PATH)
