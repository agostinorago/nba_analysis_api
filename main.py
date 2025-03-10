import os
import logging
from fastapi import FastAPI
from pydantic_settings import BaseSettings

# Configura il logging
logging.basicConfig(level=logging.INFO)

# Classe per caricare le configurazioni
class Settings(BaseSettings):
    database_url=postgresql://gioiellino_admin:LnRlKuDdE6FGiN3fuWi0L1uWhYC7Oqep@dpg-cup2amaj1k6c739f45p0-a.frankfurt-postgres.render.com/gioiello_db
    api_key:"6fb9923350bef0e66e7f17d0420511e7"

    class Config:
        env_file = ".env"  # Carica le variabili d'ambiente dal file .env
        env_file_encoding = "utf-8"

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
