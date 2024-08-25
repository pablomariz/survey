from sqlalchemy.orm import Session
from models.survey_models import Survey, SurveyData
import json

def get_survey_by_id(db: Session, survey_id: int):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if survey:
        # Formata o campo answer se necessário
        for data in survey.survey_data:
            if isinstance(data.answer, str):
                try:
                    answer_data = json.loads(data.answer)
                    # verifica se o JSON é uma lista de dicionários
                    if isinstance(answer_data, list) and all(isinstance(item, dict) for item in answer_data):
                        data.answer = json.dumps(answer_data, indent=4)
                except json.JSONDecodeError:
                    pass
    return survey


def get_all_surveys(db: Session):
    return db.query(Survey).all()


def create_survey_from_endpoint1(db: Session, survey_data: dict):
    existing_survey = db.query(Survey).filter(Survey.id == survey_data.get('id')).first()
    if existing_survey:
        # print(f"Pesquisa com ID {survey_data.get('id')} já existe. Pulando inserção.")
        return
    # Cria e adiciona a pesquisa
    survey = Survey(
        contact_id=survey_data.get('contact_id', ''),
        status=survey_data.get('status', ''),
        date_submitted=survey_data.get('date_submitted', ''),
        session_id=survey_data.get('session_id', ''),
        language=survey_data.get('language', ''),
        date_started=survey_data.get('date_started', ''),
        ip_address=survey_data.get('ip_address', ''),
        referer=survey_data.get('referer', ''),
        user_agent=survey_data.get('user_agent', ''),
        country=survey_data.get('country', '')
    )
    db.add(survey)
    db.commit()
    db.refresh(survey)

    # Cria e adiciona os dados da pesquisa
    for qid, qdata in survey_data.get('survey_data', {}).items():
        # Determine o tipo de resposta
        survey_item = SurveyData(
            survey_id=survey.id,
            question_id=qdata.get('id'),
            question_type=qdata.get('type'),
            question=qdata.get('question', ''),
            answer=json.dumps(qdata.get('answer', [])) if isinstance(qdata.get('answer'), list) else qdata.get('answer', ''),
            answer_id=qdata.get('answer_id', None),
            parent=qdata.get('parent', None),
            section_id=qdata.get('section_id', None),
            shown=qdata.get('shown', None)
        )
        db.add(survey_item)
    db.commit()


def create_survey_from_endpoint2(db: Session, survey_data: list):
    for survey in survey_data:
        existing_survey = db.query(Survey).filter(Survey.id == survey.get('id')).first()
        if existing_survey:
            # print(f"Pesquisa com ID {survey.get('id')} já existe. Pulando inserção.")
            continue

        # Cria e adiciona a pesquisa
        new_survey = Survey(
            id=int(survey.get('id', 0)),
            contact_id=survey.get('contact_id', ''),
            status=survey.get('status', ''),
            date_submitted=survey.get('date_submitted', ''),
            session_id=survey.get('session_id', ''),
            language=survey.get('language', ''),
            date_started=survey.get('date_started', ''),
            ip_address=survey.get('ip_address', ''),
            referer=survey.get('referer', ''),
            user_agent=survey.get('user_agent', ''),
            country=survey.get('country', '')
        )
        db.add(new_survey)
        db.commit()
        db.refresh(new_survey)

        # Cria e adiciona os dados da pesquisa
        for question, answer in survey.items():
            if question not in {'id', 'contact_id', 'status', 'date_submitted', 'session_id', 'language', 'date_started', 'ip_address', 'referer', 'user_agent', 'country'}:
                survey_item = SurveyData(
                    survey_id=new_survey.id,
                    question_id=None, 
                    question_type=None, 
                    question=question,
                    answer=answer,
                    answer_id=None,
                    parent=None,
                    section_id=None,
                    shown=None
                )
                db.add(survey_item)
        db.commit()


def create_survey_from_endpoint3(db: Session, survey_data: list):
    for survey in survey_data:
        existing_survey = db.query(Survey).filter(Survey.contact_id == survey.get('contact_id')).first()
        if existing_survey:
            # print(f"Pesquisa com CONTAC_ID {survey.get('contact_id')} já existe. Pulando inserção.")
            continue
        
        # Cria e adiciona a pesquisa
        new_survey = Survey(
            contact_id=survey.get('contact_id', ''),
            status=survey.get('status', ''),
            date_submitted=survey.get('date_submitted', ''),
            session_id=survey.get('session_id', ''),
            language=survey.get('language', ''),
            date_started=survey.get('date_started', ''),
            ip_address=survey.get('ip_address', ''),
            referer=survey.get('referer', ''),
            user_agent=survey.get('user_agent', ''),
            country=survey.get('country', '')
        )
        db.add(new_survey)
        db.commit()
        db.refresh(new_survey)

        # Cria e adiciona os dados da pesquisa
        for qdata in survey.get('survey_data', []):
            survey_item = SurveyData(
                survey_id=new_survey.id,
                question_id=qdata.get('id'),
                question=qdata.get('question', ''),
                answer=qdata.get('answer', ''),
                answer_id=qdata.get('answer_id', None),
                shown=qdata.get('shown', None),
                parent=None, 
                section_id=None 
            )
            db.add(survey_item)
        db.commit()

