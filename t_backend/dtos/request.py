from pydantic.main import BaseModel


class MessageRequest(BaseModel):
    chat_id: int
    content: str
