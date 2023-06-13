from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, ARRAY

## Feedback Model
# This model is used to store the feedback results in the database.
# The feedback results are stored as a string, concatenate all the result into a string with "|" delimiter.
# The target search term is stored in the database.
# The target_search_uuid is used to identify the search result.
# The feed_back_user is used to identify the user who give the feedback.

class Feedback(Base):
    __tablename__ = 'feedback'  # type: ignore
    id = Column(Integer, primary_key=True, index=True)
    target_search_uuid = Column(String, index=True)
    target_search_term = Column(String, index=True)
    target_search_result = Column(String, nullable=False)
    feed_back_user = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
