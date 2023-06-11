from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from app.db.crud.base import CRUDBase
from app.db.models.search import Search
from app.schemas.search import SearchCreate

class CRUDSearch(CRUDBase[Search, SearchCreate, SearchCreate]):
    
    def get_search_by_uuid(
        self, 
        db: Session, 
        uuid: str, 
        user: str
    ) -> Optional[Search]:
        return (
            db.query(Search)
            .filter(Search.search_uuid == uuid)
            .filter(Search.search_user == user)
            .first()
        )
    
    def get_search_count_by_term(
        self,
        db: Session,
        term: str,
        start_date: Optional[datetime],
        end_date: Optional[datetime],
    ) -> int:
        query = (
            db
            .query(Search)
            .filter(Search.search_term == term)
        )
        if start_date:
            query = query.filter(Search.created_at >= start_date)
        if end_date:
            query = query.filter(Search.created_at <= end_date)
        return query.count()


search = CRUDSearch(Search)