from fastapi import FastAPI
from api.routes import router as survey_router

app = FastAPI()

app.include_router(survey_router)