import random

from t_backend.constants import GREETING_TEXTS
from t_backend.dtos.response import ChatResponse
from t_backend.models import Chat, Message
from t_backend.repositories.chat import ChatRepository
from t_backend.repositories.message import MessageRepository


class ChatService:
    def __init__(
        self, chat_repository: ChatRepository, message_repository: MessageRepository
    ):
        self._repository = chat_repository
        self._message_repository = message_repository

    def create_chat(self) -> tuple[Chat, Message]:
        chat = self._repository.create()
        greeting_text = random.choice(GREETING_TEXTS)
        message = self._message_repository.create_message(
            chat_id=chat.id,
            content=greeting_text,
            is_user=False,
            is_complete=True,
        )
        return chat, message

    def get_chat_list(self) -> list[ChatResponse]:
        chat_tuple_list = self._repository.get_all()
        chat_list: list[ChatResponse] = []
        for chat, last_message in chat_tuple_list:
            chat = ChatResponse.from_orm(chat)
            chat.last_message = last_message
            chat_list.append(chat)
        return chat_list
