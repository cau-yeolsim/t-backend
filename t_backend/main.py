from fastapi import FastAPI
import sentry_sdk

from settings import settings
from t_backend.containers import Container
from t_backend.routers.core import router as core_router
from t_backend.routers.message import router as message_router
from t_backend.routers.chat import router as chat_router


def create_app() -> FastAPI:
    container = Container()

    fast_app = FastAPI()
    fast_app.container = container
    fast_app.include_router(core_router)
    fast_app.include_router(message_router)
    fast_app.include_router(chat_router)

    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

    return fast_app


app = create_app()
