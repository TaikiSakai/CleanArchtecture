from abc import ABC, abstractmethod

from src.entities.user import User


class UserRepositoryI(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User | None:
        """Retrieve a user by their ID."""

    @abstractmethod
    def get_users(self) -> list[User] | list[None]:
        """Retrieve all users."""

    @abstractmethod
    def create_user(self, user: User) -> User:
        """Create a new user in the repository."""

    @abstractmethod
    def update_user(self, user: User) -> User:
        """Update an existing user in the repository."""

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        """Delete a user by their ID."""
