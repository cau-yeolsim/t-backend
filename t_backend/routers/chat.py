import datetime

from fastapi import APIRouter
from fastapi import Depends

from t_backend.containers import Container
from t_backend.services.chat import ChatService
from dependency_injector.wiring import Provide, inject
from t_backend.dtos.response import ChatListResponse

router = APIRouter(prefix="/chats")


@router.post("", status_code=201)
async def create_chat():
    return {
        "id": 1,
        "title": "티로와의 이야기",
        "profile_img_url": "https://images.pexels.com/photos/1808329/pexels-photo-1808329.jpeg",
        "created_at": datetime.datetime.now(),
    }


@router.get("")
@inject
async def get_chat_list(
    chat_service: ChatService = Depends(Provide[Container.chat_service]),
) -> ChatListResponse:
    return ChatListResponse(chats=chat_service.get_chat_list())
