from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[4]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env",
                                      extra="ignore")

    DB_CONNECTION: str
    SECRET_KEY: str
    ALGORITHM: str
    EXP_TIME: int

settings = Settings()