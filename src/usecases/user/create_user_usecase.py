from datetime import datetime
from abc import ABC, abstractmethod

from src.entities.user.user import User
from src.entities.user.datas import Role
from src.entities.repositories.user import UserRepositoryI


class CreateUserUseCaseI(ABC):
    @abstractmethod
    def execute(
        self,
        user_name: str,
        email: str,
        role: Role,
        is_active: bool
    ) -> User:
        """Create a new user with the provided details."""


class CreateUserUseCase(CreateUserUseCaseI):
    def __init__(self, user_repository: UserRepositoryI):
        self.user_repository = user_repository

    def execute(
        self,
        user_name: str,
        email: str,
        role: Role,
        is_active: bool
    ) -> User:
        user = User.create(
            id=None,
            user_name=user_name,
            email=email,
            role=role,
            is_active=is_active,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        return self.user_repository.create_user(user)


def create_user_usecase_factory(user_repository: UserRepositoryI) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)
