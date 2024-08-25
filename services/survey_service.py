import requests
from repositories.survey_repository import create_survey_from_endpoint1, create_survey_from_endpoint2, create_survey_from_endpoint3
from core.config import SessionLocal
import xml.etree.ElementTree as ET

def fetch_survey_data(endpoint=1):
    url = f"https://numera-case.web.app/v1/survey/{endpoint}/answers"
    response = requests.get(url)
    response.raise_for_status()

    if endpoint == 3:
        return parse_xml_response(response.content)
    else:
        data = response.json()
        return data['data']

def parse_xml_response(xml_content):
    root = ET.fromstring(xml_content)
    survey_data = []
    
    for item in root.findall(".//data/item"):
        survey_item = {
            "contact_id": item.find("contact_id").text if item.find("contact_id") is not None else "",
            "status": item.find("status").text if item.find("status") is not None else "",
            "date_submitted": item.find("date_submitted").text if item.find("date_submitted") is not None else "",
            "session_id": item.find("session_id").text if item.find("session_id") is not None else "",
            "language": item.find("language").text if item.find("language") is not None else "",
            "date_started": item.find("date_started").text if item.find("date_started") is not None else "",
            "ip_address": item.find("ip_address").text if item.find("ip_address") is not None else "",
            "referer": item.find("referer").text if item.find("referer") is not None else "",
            "user_agent": item.find("user_agent").text if item.find("user_agent") is not None else "",
            "country": item.find("country").text if item.find("country") is not None else "",
            "survey_data": []
        }
        
        for q_item in item.findall(".//survey_data/item"):
            id = q_item.find("id").text if q_item.find("id") is not None else None  # Capturando o ID do XML
            question = q_item.find("question").text if q_item.find("question") is not None else ""
            answer = q_item.find("answer").text if q_item.find("answer") is not None else ""
            answer_id = q_item.find("answer_id").text if q_item.find("answer_id") is not None else None
            shown_str = q_item.find("shown").text if q_item.find("shown") is not None else None
            
            # Converte string 'true'/'false' em valores booleanos
            shown = shown_str.lower() == 'true' if shown_str else None

            survey_item["survey_data"].append({
                "id": int(id),
                "question": question,
                "answer": answer,
                "answer_id": answer_id,
                "shown": shown
            })
            
        survey_data.append(survey_item)
    
    return survey_data


def insert_survey_data(endpoint):
    if endpoint not in {1, 2, 3}:
        print("Endpoint não suportado")
        return  
    
    db = SessionLocal()
    try:
        survey_data = fetch_survey_data(endpoint)
        if endpoint == 1:
            for survey in survey_data:
                create_survey_from_endpoint1(db, survey)
        elif endpoint == 2:
            create_survey_from_endpoint2(db, survey_data)
        elif endpoint == 3:
            create_survey_from_endpoint3(db, survey_data)
        else:
            raise ValueError("Endpoint não suportado")
    finally:
        db.close()
