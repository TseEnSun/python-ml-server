from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class ReportBase(BaseModel):
    search_term: str
    frequency: int
    not_good_result: List[str]


class ReportRequest(BaseModel):
    search_term: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]


class ReportResponse(ReportBase):
    pass