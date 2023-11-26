import datetime

from pydantic.main import BaseModel


class MessageResponse(BaseModel):
    id: int
    content: str
    created_at: datetime.datetime
    created_by: str
    chat_id: int
    is_complete: bool | None

    class Config:
        orm_mode = True


class MessageListResponse(BaseModel):
    messages: list[MessageResponse]


class ChatResponse(BaseModel):
    id: int
    title: str
    profile_img_url: str
    created_at: datetime.datetime
    last_message: MessageResponse | None

    class Config:
        orm_mode = True


class ChatListResponse(BaseModel):
    chats: list[ChatResponse]
