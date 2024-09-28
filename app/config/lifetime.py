import asyncio
from typing import Awaitable, Callable

from fastapi import FastAPI

def register_startup_event(app: FastAPI) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        app.middleware_stack = None
        app.middleware_stack = app.build_middleware_stack()
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(app: FastAPI) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        await app.state.db_engine.dispose()
        pass  # noqa: WPS420

    return _shutdown

