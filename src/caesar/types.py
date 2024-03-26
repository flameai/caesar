from sqlalchemy.orm import Mapped

UserId = int | Mapped[int]
GroupId = int | Mapped[int]
GroupName = str | Mapped[str]
TimeLasted = int
