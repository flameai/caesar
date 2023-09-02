from pydantic import conlist
from fastapi_utils.api_model import APIModel


class ChangeMembershipRequestSchema(APIModel):
    groups: conlist(int, unique_items=True)
