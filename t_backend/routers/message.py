from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from t_backend.containers import Container
from t_backend.dtos.request import MessageRequest
from t_backend.dtos.response import MessageResponse, MessageListResponse
from t_backend.services.message import MessageService

router = APIRouter(prefix="/messages")


@router.post("/{chat_id}", status_code=201)
@inject
async def create_message(
    chat_id: int,
    message_request: MessageRequest,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageResponse:
    new_message = message_service.create_message(
        chat_id=chat_id, content=message_request.content
    )
    return MessageResponse.from_orm(new_message)


@router.get("/{chat_id}")
@inject
async def get_message_list(
    chat_id: int,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageListResponse:
    messages = message_service.get_chat_list(chat_id=chat_id)
    return MessageListResponse(messages=messages)
