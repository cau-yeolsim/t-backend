import random

from t_backend.repositories.message import MessageRepository
from t_backend.repositories.openai import OpenAIRepository


class MessageService:
    def __init__(
        self, message_repository: MessageRepository, openai_repository: OpenAIRepository
    ):
        # gpt 관련 부분 추가
        self._message_repository = message_repository
        self._openai_repository = openai_repository

    def create_message(self, chat_id: int, content: str):
        self._message_repository.create_message(
            chat_id=chat_id, content=content, is_user=True
        )  # user_message
        # TODO: 봇 메시지를 gpt 를 통해서 처리하기
        # bot message
        bot_contents = [
            "안녕하세요 저는 티로봇입니다.",
            "어떤 고민이 있으신가요?",
            "저는 아직 배우는 중이라 많이 부족해요.",
        ]
        return self._message_repository.create_message(
            chat_id=chat_id, content=random.choice(bot_contents), is_user=False
        )

    def get_message_list(self, chat_id: int):
        return self._message_repository.get_messages(chat_id=chat_id)
