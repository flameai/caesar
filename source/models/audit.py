from enum import Enum
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from source.models.base import Base


class EventType(Enum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class Audit(Base):
    __tablename__ = "audits"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[EventType]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    dt: Mapped[datetime]
    m2m_user_group_id = mapped_column(ForeignKey("m2m_users_groups"), nullable=False)
