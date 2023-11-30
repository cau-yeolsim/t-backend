import random
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import RowReturningQuery

from t_backend.alembic.utils import get_now
from t_backend.constants import TIRO_IMG_URLS
from t_backend.models import Chat, Message


class ChatRepository:
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        self.session_factory = session_factory

    def get_all(self) -> RowReturningQuery[tuple[Chat, Message]]:
        with self.session_factory() as session:
            latest_message_subquery = (
                session.query(
                    Message.chat_id, func.max(Message.id).label("latest_message_id")
                )
                .group_by(Message.chat_id)
                .subquery("latest_message")
            )

            return (
                session.query(Chat, Message)
                .outerjoin(
                    latest_message_subquery,
                    Chat.id == latest_message_subquery.c.chat_id,
                )
                .outerjoin(
                    Message, Message.id == latest_message_subquery.c.latest_message_id
                )
            ).order_by(Chat.id.desc())

    def create(self) -> Chat:
        new_chat = Chat(
            title="", profile_img_url=self._get_tiro_img_url(), created_at=get_now()
        )
        with self.session_factory() as session:
            session.add(new_chat)
            session.commit()
            new_chat.title = f"티로와의 이야기 ({new_chat.id})"
            session.commit()
            session.refresh(new_chat)
            return new_chat

    def _get_tiro_img_url(self) -> str:
        return random.choice(TIRO_IMG_URLS)
