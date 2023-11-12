from t_backend.repositories.chat import ChatRepository


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self._repository = chat_repository

    def create_chat(self):
        pass

    def get_chat_list(self):
        return self._repository.get_all()
