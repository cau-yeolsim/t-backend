from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from t_backend.containers import Container
from t_backend.dtos.request import MessageRequest
from t_backend.dtos.response import MessageResponse, MessageListResponse
from t_backend.services.message import MessageService

router = APIRouter(prefix="/messages")


@router.post("", status_code=201, summary="메시지 생성")
@inject
async def create_message(
    message_request: MessageRequest,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageResponse:
    new_message = message_service.create_message(
        chat_id=message_request.chat_id, content=message_request.content
    )
    return MessageResponse.from_orm(new_message)


@router.get("", summary="특정 채팅방 메시지 조회")
@inject
async def get_message_list(
    chat_id: int = 0,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageListResponse:
    if not chat_id:
        raise HTTPException(status_code=400, detail="채팅방 ID 가 필요합니다.")
    messages = message_service.get_message_list(chat_id=chat_id)
    return MessageListResponse(messages=messages)


@router.get("/{message_id}", summary="특정 ID 메시지 조회 (polling 시 사용)")
@inject
async def get_message(
    message_id: int,
    message_service: MessageService = Depends(Provide[Container.message_service]),
) -> MessageResponse:
    message = message_service.get_message(message_id=message_id)
    if not message:
        raise HTTPException(status_code=404, detail="해당하는 ID 의 메시지가 없습니다.")
    return MessageResponse.from_orm(message)
