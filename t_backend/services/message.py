from t_backend.repositories.message import MessageRepository


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self._repository = message_repository

    def create_message(self, chat_id: int, content: str):
        return self._repository.create(chat_id=chat_id, content=content)

    def get_chat_list(self, chat_id: int):
        return self._repository.get_all(chat_id=chat_id)
