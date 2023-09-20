from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from common.fastapi.registry import ComponentCategoryEnum, get_db

router = InferringRouter(tags=["membership", "change"])


@cbv(router)
class MembershipChangeView:
    session: AsyncSession = Depends(get_db)

    @router.post("/api/v1/membership/{user_id}")
    def change_membership(self, user_id):
        Response(status_code=200)
