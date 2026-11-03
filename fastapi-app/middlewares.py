import logging
import time

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

    @app.middleware("http")
    async def add_process_time_to_request(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.5f}"
        return response
