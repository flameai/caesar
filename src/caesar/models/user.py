from typing import List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from caesar.models.base import Base
from caesar.models.m2m_user_group import M2MUserGroup


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    groups: Mapped[List[M2MUserGroup]] = relationship()
