from fastapi import APIRouter
from app.api.api_v1.endpoints import (
    login,
    user,
    search,
    feedback,
    report,
    image,
)

api_router = APIRouter()

api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
api_router.include_router(report.router, prefix="/report", tags=["report"])
api_router.include_router(image.router, prefix="/image", tags=["image"])
