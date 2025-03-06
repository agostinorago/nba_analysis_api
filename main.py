import logging

logging.basicConfig(level=logging.INFO)
logging.info(f"DATABASE_URL: {settings.database_url}")
logging.info(f"API_KEY: {settings.api_key}")

from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

# Definizione della classe Settings utilizzando il nuovo import di BaseSettings
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    # Variabili d'ambiente obbligatorie
    database_url: str
    secret_key: str
    api_key: str

# Inizializzazione delle configurazioni
settings = Settings()

# Creazione dell'app FastAPI
app = FastAPI(title="La mia App su Render")

# Endpoint principale che restituisce le impostazioni caricate
@app.get("/")
def read_root():
    return {
        "App Name": app.title,
        "Database URL": settings.database_url,
        "Secret Key": settings.secret_key,
        "API Key": settings.api_key,
    }

# Blocco per avviare l'app in modalità sviluppo
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
