from core.config import create_database, create_tables
from services.survey_service import insert_survey_data

def main():
    create_database() 
    create_tables() 

    for endpoint in [1, 2, 3]:
        insert_survey_data(endpoint=endpoint)

if __name__ == "__main__":
    main()
