from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.entities.repositories.user import UserRepositoryI
from src.entities.user.user import User
from src.infrastructures.models.users import UsersModel


class UserRepositoryImpl(UserRepositoryI):
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self) -> list[User]:
        pass

    def get_user(self, user_id: int) -> User | None:
        user = self.db.query(UsersModel).filter(UsersModel.id == user_id).first()

        if user:
            return user.to_entity()

        raise HTTPException(status_code=404, detail="User not found")

    def create_user(self, user: Annotated[User, User]) -> User:
        user_model = UsersModel.from_entity(user)
        self.db.add(user_model)
        self.db.commit()
        self.db.flush()

        return user_model.to_entity()

    def update_user(self, user: User) -> User:
        pass

    def delete_user(self, user_id: int) -> None:
        pass


def user_repository_factory(db: Session) -> UserRepositoryImpl:
    return UserRepositoryImpl(db)
