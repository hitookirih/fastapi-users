import logging

from fastapi import FastAPI
from fastapi import Request, Response

from typing import Callable, Awaitable

log = logging.getLogger(__name__)


def register_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_new_request(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        log.info(
            "Request %s to %s",
            request.method,
            request.url,
        )
        return await call_next(request)
