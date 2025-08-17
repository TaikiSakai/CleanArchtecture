from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

    def __str__(self) -> str:
        return self.value
