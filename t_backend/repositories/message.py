from contextlib import AbstractContextManager
from typing import Callable, Type

from redis import Redis
from sqlalchemy import select
from sqlalchemy.orm import Session

from t_backend.alembic.utils import get_now
from t_backend.cipher import aes_encrypt
from t_backend.models import Message


class MessageRepository:
    _redis_client: Redis

    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
        redis_client: Redis,
    ) -> None:
        self.session_factory = session_factory
        self._redis_client = redis_client

    def get_messages(self, chat_id: int) -> list[Type[Message]]:
        stmt = (
            select(Message)
            .where(Message.chat_id == chat_id)
            .order_by(Message.id.desc())
        )
        with self.session_factory() as session:
            return list(session.scalars(stmt))

    def create_message(
        self, chat_id: int, content: str, is_user: bool, is_complete: bool = False
    ) -> Message:
        new_message = Message(
            encrypted_content=aes_encrypt(content),
            created_by="me" if is_user else "TIRO",
            created_at=get_now(),
            chat_id=chat_id,
            is_complete=is_complete or (True if is_user else False),
        )
        with self.session_factory() as session:
            session.add(new_message)
            session.commit()
            session.refresh(new_message)
            return new_message

    def get_message(self, message_id: int) -> Type[Message] | None:
        with self.session_factory() as session:
            message = session.get(Message, message_id)
            if not message:
                return None
            content = self._redis_client.get(str(message_id))
            content = content.decode("utf-8") if content else ""
            message.encrypted_content = aes_encrypt(content)
        return message

    def get_cached_message_content(self, message_id: int) -> str:
        content = self._redis_client.get(str(message_id))
        content = content.decode("utf-8") if content else ""
        return content

    def update_is_complete_true(self, message_id: int, content: str):
        with self.session_factory() as session:
            message = session.get(Message, message_id)
            message.is_complete = True
            message.encrypted_content = aes_encrypt(content)
            session.add(message)
            session.commit()
