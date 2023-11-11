import datetime

from fastapi import APIRouter

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
async def get_chat_list():
    return {
        "chats": [
            {
                "id": 1,
                "title": "티로와의 이야기",
                "profile_img_url": "https://images.pexels.com/photos/1808329/pexels-photo-1808329.jpeg",
                "created_at": datetime.datetime.now(),
            }
        ]
    }
