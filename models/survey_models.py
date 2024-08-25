from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from core.config import Base

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True) 
    contact_id = Column(String(50), index=True)
    status = Column(String(20))
    date_submitted = Column(String(50))
    session_id = Column(String(100))
    language = Column(String(20))
    date_started = Column(String(50))
    ip_address = Column(String(50))
    referer = Column(String(255))
    user_agent = Column(String(255))
    country = Column(String(50))

    survey_data = relationship("SurveyData", back_populates="survey")

class SurveyData(Base):
    __tablename__ = "survey_data"

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    question_id = Column(Integer, nullable=True) 
    question_type = Column(String(20), nullable=True) 
    parent = Column(Integer, nullable=True)
    question = Column(Text)
    section_id = Column(Integer, nullable=True)
    answer = Column(Text)
    answer_id = Column(Integer, nullable=True)
    shown = Column(Boolean, nullable=True)

    survey = relationship("Survey", back_populates="survey_data")
