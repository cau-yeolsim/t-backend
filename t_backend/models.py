from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text

from .database import Base


class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    profile_img_url = Column(String(length=2048))
    created_at = Column(DateTime)


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_by = Column(String(length=20))
    chat_id = Column(Integer, ForeignKey("chat.id"))
