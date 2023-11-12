from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter
from fastapi import Depends

from t_backend.containers import Container
from t_backend.dtos.response import ChatListResponse, ChatResponse
from t_backend.services.chat import ChatService

router = APIRouter(prefix="/chats")


@router.post("", status_code=201)
@inject
async def create_chat(
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> ChatResponse:
    return ChatResponse.from_orm(chat_service.create_chat())


@router.get("")
@inject
async def get_chat_list(
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> ChatListResponse:
    return ChatListResponse(chats=chat_service.get_chat_list())
