import os
import logging
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

# Configura il logging
logging.basicConfig(level=logging.INFO)

# Classe per caricare le configurazioni
class Settings(BaseSettings):
    database_url: str
    api_key: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Inizializza le configurazioni
settings = Settings()

# Log delle configurazioni
logging.info(f"DATABASE_URL: {settings.database_url}")
logging.info(f"API_KEY: {settings.api_key}")

# Crea l'app FastAPI
app = FastAPI(title="La mia App su Render")

@app.get("/")
def read_root():
    return {
        "API Key": settings.api_key,
    }

# Avvio dell'app con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

