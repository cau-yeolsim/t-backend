import random
from threading import Thread
from typing import Type

from t_backend.models import Message
from t_backend.repositories.message import MessageRepository
from t_backend.repositories.openai import OpenAIRepository


class MessageService:
    def __init__(
        self, message_repository: MessageRepository, openai_repository: OpenAIRepository
    ):
        # gpt 관련 부분 추가
        self._message_repository = message_repository
        self._openai_repository = openai_repository

    def create_message(self, chat_id: int, content: str) -> Message:
        # user_message
        self._message_repository.create_message(
            chat_id=chat_id, content=content, is_user=True
        )
        # bot message
        message = self._message_repository.create_message(
            chat_id=chat_id, content="", is_user=False
        )
        thread = Thread(
            target=self._openai_repository.send_message, args=(message.id, content)
        )
        thread.start()
        return message

    def get_message_list(self, chat_id: int) -> list[Type[Message]]:
        return self._message_repository.get_messages(chat_id=chat_id)

    def get_message(self, message_id: int) -> Type[Message] | None:
        return self._message_repository.get_message(message_id=message_id)
