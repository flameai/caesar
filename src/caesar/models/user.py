from typing import List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from caesar.models.base import Base
from caesar.models.m2m_user_group import M2MUserGroup
from caesar.types import UserId


class User(Base):
    __tablename__ = "users"

    id: UserId = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    groups: Mapped[List[M2MUserGroup]] = relationship()
