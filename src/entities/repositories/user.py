from abc import ABC, abstractmethod
from typing import List, Optional

from src.entities.user.user import User


class UserRepositoryI(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""
    
    @abstractmethod
    def create_user(self, user: User) -> User:
        """Create a new user in the repository."""

    @abstractmethod
    def update_user(self, user: User) -> User:
        """Update an existing user in the repository."""

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        """Delete a user by their ID."""

    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Retrieve all users in the repository."""
