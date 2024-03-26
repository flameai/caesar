from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from caesar.models.base import Base
from caesar.types import GroupId, GroupName


class Group(Base):
    __tablename__ = "groups"
    id: GroupId = mapped_column(primary_key=True)
    name: GroupName = mapped_column(String(64))
