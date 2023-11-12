from t_backend.dtos.response import ChatResponse
from t_backend.repositories.chat import ChatRepository


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self._repository = chat_repository

    def create_chat(self):
        return self._repository.create()

    def get_chat_list(self) -> list[ChatResponse]:
        chat_tuple_list = self._repository.get_all()
        chat_list: list[ChatResponse] = []
        for chat, last_message in chat_tuple_list:
            chat = ChatResponse.from_orm(chat)
            chat.last_message = last_message
            chat_list.append(chat)
        return chat_list
