from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.db import models, crud
from app import schemas
from app.services.image_search import searcher


router = APIRouter()

@router.post("", response_model=schemas.SearchResponse)
def search(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_active_user_by_header),
    search_request: schemas.SearchRequest,
) -> Any:
    """
    Search for a term
    """
    search_result = searcher.search(search_request.search_term).tolist()
    search_obj = schemas.SearchCreate(
        search_term=search_request.search_term,
        search_result="|".join([str(x) for x in search_result]),
        search_user=current_user.email
    )
    search_in_db = crud.search.create(db, obj_in=search_obj)
    
    return {
        "search_uuid": search_in_db.search_uuid,
        "search_term": search_in_db.search_term,
        "search_result": search_in_db.search_result
    }