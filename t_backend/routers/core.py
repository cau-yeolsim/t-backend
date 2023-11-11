import time

from fastapi import APIRouter, Response
from fastapi.routing import APIRoute


class TimedRoute(APIRoute):
    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request):
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            return response

        return custom_route_handler


router = APIRouter(route_class=TimedRoute)


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/error")
async def error():
    raise AssertionError
