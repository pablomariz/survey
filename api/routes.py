from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from core.config import SessionLocal
from repositories.survey_repository import get_survey_by_id, get_all_surveys
from schemas.survey_schema import Survey
from utils.utils import format_answer
from typing import List


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/surveys/{survey_id}", response_model=Survey)
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = get_survey_by_id(db, survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    # Formatar os dados das pesquisas
    for data in survey.survey_data:
        data.answer = format_answer(data.answer)  # Formata o campo answer
    
    return survey


@router.get("/surveys/", response_model=List[Survey])
def read_all_surveys(db: Session = Depends(get_db)):
    surveys = get_all_surveys(db)
    if not surveys:
        raise HTTPException(status_code=404, detail="No surveys found")
    
    # Formatar os dados das pesquisas
    for survey in surveys:
        for data in survey.survey_data:
            data.answer = format_answer(data.answer)  # Formata o campo answer
    
    return surveys