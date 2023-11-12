import random

from t_backend.repositories.message import MessageRepository


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self._repository = message_repository

    def create_message(self, chat_id: int, content: str):
        self._repository.create_message(
            chat_id=chat_id, content=content, is_user=True
        )  # user_message

        # bot message
        bot_contents = [
            "안녕하세요 저는 티로봇입니다.",
            "어떤 고민이 있으신가요?",
            "저는 아직 배우는 중이라 많이 부족해요.",
        ]
        return self._repository.create_message(
            chat_id=chat_id, content=random.choice(bot_contents), is_user=False
        )

    def get_chat_list(self, chat_id: int):
        return self._repository.get_messages(chat_id=chat_id)
