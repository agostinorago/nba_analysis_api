from fastapi import FastAPI
from pydantic import BaseSettings

# Definizione della classe Settings per caricare le configurazioni dall'ambiente
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    api_key: str

    class Config:
        # Se esiste il file .env, Pydantic lo caricherà automaticamente
        env_file = ".env"
        env_file_encoding = "utf-8"

# Inizializzazione delle impostazioni
settings = Settings()

# Creazione dell'app FastAPI
app = FastAPI(title="La mia App su Render")

# Endpoint principale per verificare le configurazioni caricate
@app.get("/")
def read_root():
    return {
        "App Name": app.title,
        "Database URL": settings.database_url,
        "Secret Key": settings.secret_key,
        "API Key": settings.api_key
    }

# Avvio dell'applicazione nel caso si esegua questo file direttamente (utile per test in locale)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
