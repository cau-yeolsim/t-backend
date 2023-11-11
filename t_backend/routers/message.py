from fastapi import APIRouter

router = APIRouter(prefix="/messages")


@router.post("", status_code=201)
async def create_message():
    return {
        "id": 1,
        "content": "안녕하세요 저는 티로에요! 아직 말을 할 줄 모른답니다 ㅎㅎ",
        "created_by": "TIRO",
        "chat_id": 1,
    }


@router.get("/{chat_id}")
async def get_message_list(chat_id: int):
    """

    :param chat_id: 채팅방 id
    :return: 채팅의 메시지 리스트를 반환합니다.
    """
    return {
        "chat_id": chat_id,
        "messages": [
            {
                "id": 1,
                "content": "안녕하세요 저는 티로에요! 아직 말을 할 줄 모른답니다 ㅎㅎ",
                "created_by": "TIRO",
                "chat_id": 1,
            }
        ],
    }
