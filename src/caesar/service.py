from caesar.models.group import Group
from caesar.models.user import User
from caesar.types import GroupId, GroupName, UserId


class CaesarService:
    def change_user_memberships(
        self, user_id: UserId, group_ids: list[GroupId]
    ) -> None:
        pass

    def change_group_members(self, group_id: GroupId, user_ids: list[UserId]) -> None:
        pass

    def get_group_members_by_name(self, group_name: GroupName) -> list[User]:
        pass

    def get_user_groups_by_id(self, user_id: UserId) -> list[Group]:
        pass


caesar_service = CaesarService()
