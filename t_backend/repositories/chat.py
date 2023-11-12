from contextlib import AbstractContextManager
from typing import Callable, Type

from sqlalchemy.orm import Session

from t_backend.alembic.utils import get_now
from t_backend.models import Chat


class ChatRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self) -> list[Type[Chat]]:
        with self.session_factory() as session:
            return session.query(Chat).all()

    def create(self) -> Chat:
        new_chat = Chat(title="", profile_img_url="", created_at=get_now())
        with self.session_factory() as session:
            session.add(new_chat)
            session.commit()
            new_chat.title = f"티로와의 이야기 ({new_chat.id})"
            session.commit()
            session.refresh(new_chat)
            return new_chat
