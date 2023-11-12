from pydantic.main import BaseModel


class MessageRequest(BaseModel):
    content: str
