from pydantic import BaseModel
from typing import List, Optional, Union

class SurveyData(BaseModel):
    question: str
    answer: Optional[Union[str, List[dict]]]
    answer_id: Optional[int] = None
    shown: Optional[bool] = None


class Survey(BaseModel):
    contact_id: str
    status: str
    date_submitted: str
    session_id: str
    language: str
    date_started: str
    ip_address: str
    referer: str
    user_agent: str
    country: str
    survey_data: List[SurveyData]
