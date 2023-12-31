from dotenv import load_dotenv
from pydantic import (
    BaseSettings,
    Field,
)


load_dotenv()


class ProjectSettings(BaseSettings):
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    SENTRY_DSN: str = Field(..., env="SENTRY_DSN")
    SQLALCHEMY_DATABASE_URL: str = Field(..., env="SQLALCHEMY_DATABASE_URL")
    REDIS_URL: str = Field(..., env="REDIS_URL")
    REDIS_PORT: int = Field(..., env="REDIS_PORT")
    AES_KEY: bytes = Field(..., env="AES_KEY")


settings = ProjectSettings()
