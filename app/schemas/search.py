from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, UUID4

class SearchBase(BaseModel):
    search_term: str
    search_result: str
    search_user: EmailStr


class SearchCreate(SearchBase):
    pass


class SearchInDBBase(SearchBase):
    id: int

    class Config:
        orm_mode = True


class SearchRequest(BaseModel):
    search_term: str


class SearchResponse(SearchRequest):
    search_uuid: str
    search_result: List[str]


class SearchInDB(SearchInDBBase):
    created_at: datetime
