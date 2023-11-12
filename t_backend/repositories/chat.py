from contextlib import AbstractContextManager
from typing import Callable, Type

from sqlalchemy.orm import Session

from t_backend.models import Chat


class ChatRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self) -> list[Type[Chat]]:
        with self.session_factory() as session:
            return session.query(Chat).all()
