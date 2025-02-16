from fastapi import FastAPI
from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    secret_key: str = os.getenv("SECRET_KEY")
    api_key: str = os.getenv("API_KEY")

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "Database URL": settings.database_url,
        "API Key": settings.api_key
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
