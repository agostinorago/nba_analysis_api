logging.basicConfig(level=logging.INFO)
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

# Configuro il logging per stampare i messaggi a console
logging.basicConfig(level=logging.INFO)

# Definizione della classe Settings per caricare le configurazioni dall'ambiente o dal file .env in locale
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    # Variabili d'ambiente obbligatorie
    database_url: str
    secret_key: str
    api_key: str

# Istanziazione delle configurazioni
settings = Settings()

# Stampo a log la variabile per verificare che sia stata letta correttamente
logging.info(f"DATABASE_URL: {settings.database_url}")

# Creazione dell'app FastAPI
app = FastAPI(title="La mia App su Render")

# Endpoint principale per verificare le impostazioni
@app.get("/")
def read_root():
    return {
        "App Name": app.title,
        "Database URL": settings.database_url,
        "Secret Key": settings.secret_key,
        "API Key": settings.api_key,
    }

# Blocco per avviare l'app in modalità sviluppo tramite Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
