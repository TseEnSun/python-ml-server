from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, UUID4


class FeedbackBase(BaseModel):
    target_search_term: str
    target_search_result: List[str]
    feed_back_user: EmailStr


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(FeedbackBase):
    target_search_uuid: UUID4
    target_search_result: List[str]
    feed_back_user: EmailStr


class FeedbackInDBBase(FeedbackBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
        
class FeedbackInDB(FeedbackInDBBase):
    pass


class FeedbackRequest(BaseModel):
    target_search_uuid: UUID4
    not_good_result: List[str]


class FeedbackResponse(BaseModel):
    success: bool
    message: Optional[str] = None