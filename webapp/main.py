from fastapi import FastAPI

from webapp import endpoints
from webapp.containers import Container


def create_app() -> FastAPI:
    container = Container()

    fast_app = FastAPI()
    fast_app.container = container
    fast_app.include_router(endpoints.router)

    return fast_app


app = create_app()
