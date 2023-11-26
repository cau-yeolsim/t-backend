from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship

from .database import Base
from .cipher import aes_decrypt


class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    profile_img_url = Column(String(length=2048))
    created_at = Column(DateTime)

    messages = relationship("Message", back_populates="chat")


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    encrypted_content = Column(Text)
    created_by = Column(String(length=20))
    created_at = Column(DateTime)
    chat_id = Column(Integer, ForeignKey("chat.id"))
    is_complete = Column(Boolean)

    chat = relationship("Chat", back_populates="messages")

    @property
    def content(self):
        return aes_decrypt(self.encrypted_content)
