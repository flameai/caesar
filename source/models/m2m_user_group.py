from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Index

from source.models.base import Base


class M2MUserGroup(Base):
    __tablename__ = "m2m_users_groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), index=True)

    __table_args__ = (Index('user_group_together', "user_id", "group_id"), )
