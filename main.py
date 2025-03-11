import os
import logging
from fastapi import FastAPI
from pydantic_settings import BaseSettings

# Configura il logging
logging.basicConfig(level=logging.INFO)

# Classe per caricare le configurazioni dal file .env
class Settings(BaseSettings):
    database_url: str
    api_key: str

    class Config:
        env_file = ".env"  # Carica le variabili d'ambiente dal file .env
        env_file_encoding = "utf-8"

# Inizializza le configurazioni
settings = Settings()

# Log (senza stampare dati sensibili)
logging.info("Configurazione caricata con successo!")

# Crea l'app FastAPI
app = FastAPI(title="La mia API")
