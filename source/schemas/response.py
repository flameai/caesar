from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str


class GroupResponse(BaseModel):
    id: int
    name: str
