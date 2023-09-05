from typing import List

from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends
from sqlalchemy import Select

from common.fastapi.config import ComponentCategoryGetterEnum, get_component

from source.models.group import Group
from source.schemas.response import GroupResponse

router = InferringRouter()


@cbv(router)
class GroupsView:
    session: Depends(get_component(ComponentCategoryGetterEnum.RelationalDB))

    @router.get("/groups")
    async def get_group_list(self) -> List[GroupResponse]:
        stmt = Select(Group)
        db_res = await self.session.execute(stmt)
        scalar_res = db_res.scalars().all()

        return GroupResponse.from_orm(scalar_res)
