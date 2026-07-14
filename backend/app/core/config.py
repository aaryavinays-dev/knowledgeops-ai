from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "KnowledgeOps AI Backend"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"


settings = Settings()