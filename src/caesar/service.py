from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from common.fastapi.registry import get_db
from sqlalchemy import select

from caesar.environ import MEMBERSHIP_CHANGING_STRATEGY, MembershipChangingStrategyType
from caesar.exceptions import GroupDoesntExistError, UserDoesntExistError
from caesar.models.group import Group
from caesar.models.user import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from caesar.types import GroupId, GroupName, UserId


class BaseMembershipChanger(ABC):
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    @abstractmethod
    async def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def change_group_members(
        self, group_id: GroupId, user_ids: list[UserId]
    ) -> None:
        raise NotImplementedError


class TransactionMembershipChanger(BaseMembershipChanger):
    """
    Реализует стратегию либо поменяли все группы для пользователя,
    либо вернули отказ при наличии хотябы одной ошибки
    """

    async def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None: ...


class DetailedMembershipChanger(BaseMembershipChanger):
    """
    Реализует стратегию поменять возможные для изменения в текущий момент
    членства
    """

    async def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None: ...


membership_changer_mapping = {
    MembershipChangingStrategyType.Transactional: TransactionMembershipChanger,
    MembershipChangingStrategyType.Detailed: DetailedMembershipChanger,
}


class CaesarService:
    """
    Бизнес-логика инкапсулирована в классе сервисного слоя
    как и завещал нам М.Фаулер
    """

    membership_changer: BaseMembershipChanger

    def __init__(self) -> None:
        db = get_db()
        self._db: AsyncSession = db
        self.membership_changer = membership_changer_mapping[
            MEMBERSHIP_CHANGING_STRATEGY
        ]

    def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None:
        pass

    def change_group_members(
        self, group_id: GroupId, user_ids: list[UserId]
    ) -> None: ...

    def get_group_members_by_name(self, group_name: GroupName) -> list[User]:
        return []

    def get_user_groups_by_id(self, user_id: UserId) -> list[Group]:
        return []

    def is_user_available_to_group_joining(
        self, user_id: UserId, group_id: GroupId
    ) -> bool:
        return True  # TODO: fill with logic

    def available_group_list_for_user_joining(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> list[GroupId]:
        return []

    async def get_user_by_id(self, user_id: UserId) -> User:
        session = self._db
        stmt = select(User).where(User.id == user_id)
        user = (await session.execute(stmt)).scalars().one()
        if not user:
            raise UserDoesntExistError
        return user

    async def get_group_by_name(self, group_name: GroupName) -> Group:
        session = self._db
        stmt = select(Group).where(Group.name == group_name)
        group = (await session.execute(stmt)).scalars().one()
        if not group:
            raise GroupDoesntExistError
        return group


caesar_service = CaesarService()
