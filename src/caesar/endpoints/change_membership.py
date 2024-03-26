from common.fastapi.registry import get_db
from fastapi import Depends, Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.ext.asyncio import AsyncSession

from caesar.types import UserId

router = InferringRouter(tags=["membership", "change"])


@cbv(router)
class MembershipChangeView:
    session: AsyncSession = Depends(get_db)

    @router.post("/api/v1/users/{user_id:int}/change_membership")
    def change_membership(self, user_id: UserId) -> Response:
        return Response(status_code=200)
