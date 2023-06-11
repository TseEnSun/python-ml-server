from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, ARRAY

class Feedback(Base):
    __tablename__ = 'feedback'  # type: ignore
    id = Column(Integer, primary_key=True, index=True)
    target_search_uuid = Column(Integer, index=True)
    target_search_term = Column(String, index=True)
    target_search_result = Column(ARRAY(String), nullable=False)
    feed_back_user = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
