from fastapi import APIRouter
from pydantic import BaseModel

from backend.repository import Repository


class PingResponse(BaseModel):  # noqa: D101
    message: str


def get_ping_router(_repoository: Repository) -> APIRouter:
    """Create a router for the ping endpoint.

    Returns:
        APIRouter: The router for the ping endpoint.

    """
    router = APIRouter(prefix="/ping", tags=["ping"])

    @router.get("")
    async def ping() -> PingResponse:
        return PingResponse(message="pong")

    return router
