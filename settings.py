from dotenv import load_dotenv
from pydantic import (
    BaseSettings,
    Field,
)


load_dotenv()


class ProjectSettings(BaseSettings):
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    SENTRY_DSN: str = Field(..., env="SENTRY_DSN")


settings = ProjectSettings()
