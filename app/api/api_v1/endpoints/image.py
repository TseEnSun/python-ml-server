from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from typing import Any
from app.api import deps
from app.db import models
from app.services.image_search import FILEPATHS

router = APIRouter()

@router.get("/{image_id}")
def get_image(
    *,
    image_id: int,
    current_user: models.User = Depends(deps.get_active_user_by_header),
) -> Any:
    """
    Get image by id
    """
    try:
        image_path = FILEPATHS[image_id]
        def get_image_stream():
            with open(image_path, "rb") as image:
                yield from image
        return StreamingResponse(get_image_stream(), media_type="image/jpg")
    
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Image not found",
        )

