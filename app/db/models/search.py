from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY

from app.db.base_class import Base

## Search Model
# This model is used to store the search results in the database.
# The search results are stored as a string, concatenate all the result into a string with "|" delimiter.
# The search term and user are also stored in the database.
# The search_uuid is used to identify the search result.

class Search(Base):
    __tablename__ = 'search'  # type: ignore
    id = Column(Integer, primary_key=True)
    search_uuid = Column(String, index=True, unique=True, nullable=False, default=lambda: str(uuid4()))
    search_term = Column(String, index=True)
    search_result = Column(String, nullable=False)
    search_user = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
