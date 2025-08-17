from pydantic import BaseModel, Field

from src.entities.user import User
from src.entities.user.datas import Role


class UserSchema(BaseModel):
    id: int | None
    user_name: str
    email: str
    role: str
    is_active: bool

    @staticmethod
    def from_entity(user: User) -> "UserSchema":
        return UserSchema(
            id=user.id,
            user_name=user.user_name,
            email=user.email,
            role=user.role,
            is_active=user.is_active
        )


class UserCreateSchema(BaseModel):
    user_name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=1, max_length=100)
    role: Role = Field(..., description="User role, e.g., 'admin', 'user'")
    is_active: bool = True
