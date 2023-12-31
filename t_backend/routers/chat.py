from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter
from fastapi import Depends

from t_backend.containers import Container
from t_backend.dtos.response import ChatListResponse, ChatResponse
from t_backend.services.chat import ChatService

router = APIRouter(prefix="/chats")


@router.post("", status_code=201, summary="채팅방 생성")
@inject
async def create_chat(
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> ChatResponse:
    chat, message = chat_service.create_chat()
    return ChatResponse(
        id=chat.id,
        title=chat.title,
        profile_img_url=chat.profile_img_url,
        created_at=chat.created_at,
        last_message=message,
    )


@router.get("", summary="채팅방 목록 조회")
@inject
async def get_chat_list(
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> ChatListResponse:
    return ChatListResponse(chats=chat_service.get_chat_list())
