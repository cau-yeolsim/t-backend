from dotenv import load_dotenv
from pydantic import (
    BaseSettings,
    Field,
)


load_dotenv()


class ProjectSettings(BaseSettings):
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")


project_settings = ProjectSettings().dict()
