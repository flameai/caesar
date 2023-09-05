from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from common.fastapi.config import ComponentCategoryGetterEnum, get_component

from source.deps import get_actor_id_from_header
from source.schemas.request import ChangeMembershipRequestSchema

router = InferringRouter(tags=["membership", "change"])


@cbv(router)
class MembershipChangeView:
    session: AsyncSession = Depends(get_component(ComponentCategoryGetterEnum.RelationalDB))
    actor_id: int = Depends(get_actor_id_from_header)

    @router.post("/api/v1/membership/{user_id}")
    def change_membership(self, user_id, groups: ChangeMembershipRequestSchema):
        Response(status_code=200)
