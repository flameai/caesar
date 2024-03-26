from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from caesar.models.base import Base
from caesar.models.m2m_user_group import M2MUserGroup
from caesar.types import UserId


class User(Base):
    __tablename__ = "users"

    id: Mapped[UserId] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    groups: Mapped[list[M2MUserGroup]] = relationship()
