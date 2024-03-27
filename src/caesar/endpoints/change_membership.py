from common.fastapi.registry import get_db
from fastapi import Depends, Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.ext.asyncio import AsyncSession

from caesar.exceptions import UserDoesntExistError
from caesar.schemas.request import ChangeUserMembershipsRequestSchema
from caesar.service import caesar_service
from caesar.types import UserId

router = InferringRouter(tags=["membership", "change"])


@cbv(router)
class MembershipChangeView:
    session: AsyncSession = Depends(get_db)

    @router.post("/api/v1/users/{user_id:int}/change_memberships")
    async def change_membership(
        self, user_id: UserId, data: ChangeUserMembershipsRequestSchema
    ) -> Response:
        group_ids = data.group_ids
        try:
            await caesar_service.membership_changer.change_user_memberships(
                user_id=user_id, group_ids=group_ids
            )
        except UserDoesntExistError:
            return Response(status_code=404)
        return Response(status_code=200)
