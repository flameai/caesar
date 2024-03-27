from fastapi_utils.api_model import APIModel
from pydantic import conlist

from caesar.types import GroupId, UserId


class ChangeUserMembershipsRequestSchema(APIModel):
    group_ids: conlist(GroupId, unique_items=True)


class ChangeGroupMembersRequestSchema(APIModel):
    user_ids: conlist(UserId, unique_items=True)
