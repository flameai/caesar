from typing import Annotated

from fastapi import Header


def get_actor_id_from_header(x_actor_id: Annotated[str | None, Header()] = None) -> int:
    return x_actor_id
