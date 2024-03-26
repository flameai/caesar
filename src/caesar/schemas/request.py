from fastapi_utils.api_model import APIModel
from pydantic import conlist


class ChangeMembershipRequestSchema(APIModel):
    groups: conlist(int, unique_items=True)
