from typing import Annotated

from fastapi import Header
from sqlalchemy.ext.asyncio import AsyncSession


def get_actor_id_from_header(x_actor_id: Annotated[str | None, Header()] = None) -> int:
    return x_actor_id


def get_session() -> AsyncSession:
    pass
