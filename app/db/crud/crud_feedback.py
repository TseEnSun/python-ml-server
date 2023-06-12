from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from app.db.crud.base import CRUDBase
from app.db.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate, FeedbackUpdate


class CRUDFeedback(CRUDBase[Feedback, FeedbackCreate, FeedbackUpdate]):
    
	def get_by_user_and_search(
		self, 
	    db: Session,
	    email: str, 
	    search_uuid: str
	) -> Optional[Feedback]:
		return (
			db
	        .query(self.model)
			.filter(self.model.feed_back_user == email)
			.filter(self.model.target_search_uuid == search_uuid)
			.first()
		)
	
	def get_by_search_term(
		self, 
		db: Session, 
	    search_term: str,
	    start_date: Optional[datetime],
	    end_date: Optional[datetime],
	) -> List[Feedback]:
		query = (
			db
	        .query(self.model)
	        .filter(self.model.target_search_term == search_term)
        )
		if start_date:
			query = query.filter(self.model.created_at >= start_date)
		if end_date:
			query = query.filter(self.model.created_at <= end_date)
		return query.all()
	
	def create(self, db: Session, *, obj_in: FeedbackCreate) -> Feedback:
		db_obj = Feedback(
			target_search_uuid=str(obj_in.target_search_uuid),
			target_search_term=obj_in.target_search_term,
			target_search_result=obj_in.target_search_result,
			feed_back_user=obj_in.feed_back_user
		)
		db.add(db_obj)
		db.commit()
		db.refresh(db_obj)
		return db_obj

feedback = CRUDFeedback(Feedback)
