from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from t_backend.containers import Container
from t_backend.dtos.request import MessageRequest
from t_backend.dtos.response import MessageResponse, MessageListResponse
from t_backend.services.message import MessageService

router = APIRouter(prefix="/messages")


@router.post("/chat/{chat_id}", status_code=201)
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


@router.get("/chat/{chat_id}")
@inject
async def get_message_list(
    chat_id: int,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageListResponse:
    messages = message_service.get_message_list(chat_id=chat_id)
    return MessageListResponse(messages=messages)


@router.get("/message/{message_id}")
@inject
async def get_message_list(
    message_id: int,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageResponse:
    message = message_service.get_message(message_id=message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return MessageResponse.from_orm(message)
