from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[4]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env",
                                      extra="ignore")

    DB_CONNECTION:str

settings = Settings()