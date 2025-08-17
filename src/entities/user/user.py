from datetime import datetime


class User:
    def __init__(
        self,
        user_name: str,
        email: str,
        role: str,
        id: int | None = None,
        is_active: bool = True,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now()
    ) -> None:
        self._id = id
        self._user_name = user_name
        self._email = email
        self._role = role
        self._is_active = is_active
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def user_name(self) -> str:
        return self._user_name

    @property
    def email(self) -> str:
        return self._email

    @property
    def role(self) -> str:
        return self._role

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @staticmethod
    def create(
        id: int | None,
        user_name: str,
        email: str,
        role: str,
        is_active: bool,
        created_at: datetime | None,
        updated_at: datetime | None
    ) -> 'User':
        return User(
            id=id,
            user_name=user_name,
            email=email,
            role=role,
            is_active=is_active,
            created_at=created_at or datetime.now(),
            updated_at=updated_at or datetime.now()
        )
