from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.db import models, crud
from app import schemas

router = APIRouter()

@router.post("", response_model=schemas.FeedbackResponse)
def receive_feedback(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_active_user_by_header),
    feedback_request: schemas.FeedbackRequest,
) -> Any:
    """
    Receive feedback from user
    """
    search_in_db = crud.search.get_search_by_uuid(
        db, 
        uuid=str(feedback_request.target_search_uuid),
        user=current_user.email)
    if not search_in_db:
        return {
            "success": False,
            "message": "Search not found"
        }
    if not set(
        feedback_request.not_good_result
    ).issubset(set(search_in_db.search_result)):
        return {
            "success": False,
            "message": "Not good result not in search result"
        }

    feedback_obj = schemas.FeedbackCreate(
        target_search_term=search_in_db.search_term,
        target_search_result=feedback_request.not_good_result,
        feed_back_user=current_user.email
    )
    feedback_in_db = crud.feedback.create(db, obj_in=feedback_obj)
    return {
        "success": True
    }