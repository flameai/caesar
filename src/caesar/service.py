from abc import ABC, abstractmethod

from common.fastapi.registry import get_db

from caesar.models.group import Group
from caesar.models.user import User
from caesar.types import GroupId, GroupName, UserId


class CaesarService:
    """
    Бизнес-логика инкапсулирована в классе сервисного слоя
    как и завещал нам М.Фаулер ))
    """

    def __init__(self) -> None:
        self._db = get_db()

    def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None:
        pass

    def change_group_members(self, group_id: GroupId, user_ids: list[UserId]) -> None:
        ...

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

    def get_user_by_id(self, user_id: UserId) -> User:
        return User()


caesar_service = CaesarService()


class BaseMembershipChanger(ABC):
    @abstractmethod
    def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def change_group_members(self, group_id: GroupId, user_ids: list[UserId]) -> None:
        raise NotImplementedError
