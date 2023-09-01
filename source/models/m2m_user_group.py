from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from source.models.base import Base


class M2MUserGroup(Base):
    __tablename__ = "m2m_users_groups"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), primary_key=True)
