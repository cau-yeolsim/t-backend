from sqlalchemy import select
from contextlib import AbstractContextManager
from typing import Callable, Type

from sqlalchemy.orm import Session

from t_backend.alembic.utils import get_now
from t_backend.models import Message


class MessageRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_messages(self, chat_id: int) -> list[Type[Message]]:
        stmt = (
            select(Message)
            .where(Message.chat_id == chat_id)
            .order_by(Message.id.desc())
        )
        with self.session_factory() as session:
            return list(session.scalars(stmt))

    def create_message(self, chat_id: int, content: str, is_user: bool) -> Message:
        new_message = Message(
            content=content,
            created_by="USER" if is_user else "TIRO",
            created_at=get_now(),
            chat_id=chat_id,
        )
        with self.session_factory() as session:
            session.add(new_message)
            session.commit()
            session.refresh(new_message)
            return new_message
