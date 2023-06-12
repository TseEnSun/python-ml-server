from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Any, Set
from app.api import deps
from app.db import models, crud
from app import schemas

router = APIRouter()

@router.post("", response_model=schemas.ReportResponse)
def report(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_active_superuser_by_header),
    report_request: schemas.ReportRequest,
) -> Any:
    """
    Report a search
    """
    search_term_count = crud.search.get_search_count_by_term(
        db,
        term=report_request.search_term,
        start_date=report_request.start_date,
        end_date=report_request.end_date
    )
    feedback_in_db = crud.feedback.get_by_search_term(
        db,
        search_term=report_request.search_term,
        start_date=report_request.start_date,
        end_date=report_request.end_date
    )
    not_good_result: Set[str] = set()
    for feedback in feedback_in_db:
        not_good_result.update(feedback.target_search_result.split("|"))

    report = schemas.ReportResponse(
        search_term=report_request.search_term,
        frequency=search_term_count,
        not_good_result=list(not_good_result)
    )
    return report