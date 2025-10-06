from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "API REST - Loja"
    DATABASE_URL: str = "sqlite:///./loja.db"

# objeto settings da classe Settings
settings = Settings()
