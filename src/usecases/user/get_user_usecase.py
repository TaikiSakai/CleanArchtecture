from abc import ABC, abstractmethod

from src.entities.repositories.user import UserRepositoryI
from src.entities.user import User
from src.entities.exceptions.user import UserNotFoundError


class GetUserUseCaseI(ABC):
    @abstractmethod
    def execute(self, user_id: int) -> User | None:
        """Retrieve a user by their ID."""


class GetUserUseCase(GetUserUseCaseI):
    def __init__(self, user_repository: UserRepositoryI):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        user = self.user_repository.get_user(user_id)

        if user is None:
            raise UserNotFoundError(user_id)

        return user


def create_get_user_usecase_factory(user_repository: UserRepositoryI) -> GetUserUseCase:
    return GetUserUseCase(user_repository)
