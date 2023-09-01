from typing import List
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import String

from source.models.base import Base


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
