from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from caesar.models.base import Base
from caesar.types import GroupId, GroupName


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[GroupId] = mapped_column(primary_key=True)
    name: Mapped[GroupName] = mapped_column(String(64))
