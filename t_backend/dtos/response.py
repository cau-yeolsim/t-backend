import datetime

from pydantic.main import BaseModel


class ChatResponse(BaseModel):
    id: int
    title: str
    profile_img_url: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class ChatListResponse(BaseModel):
    chats: list[ChatResponse]
