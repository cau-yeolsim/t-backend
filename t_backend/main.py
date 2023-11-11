from fastapi import FastAPI
import sentry_sdk

from settings import settings
from t_backend import endpoints
from t_backend.containers import Container


def create_app() -> FastAPI:
    container = Container()

    fast_app = FastAPI()
    fast_app.container = container
    fast_app.include_router(endpoints.router)

    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

    return fast_app


app = create_app()
