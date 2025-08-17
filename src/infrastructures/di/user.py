from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.infrastructures.postgresql.user import UserRepositoryImpl, user_repository_factory
from src.usecases.user.create_user_usecase import CreateUserUseCase, create_user_usecase_factory
from src.usecases.user.get_user_usecase import GetUserUseCase, create_get_user_usecase_factory


def get_user_repository(db: Session = Depends(get_db)) -> UserRepositoryImpl:
    return user_repository_factory(db)


def get_get_user_usecase(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> GetUserUseCase:
    return create_get_user_usecase_factory(user_repository)


def get_create_user_usecase(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> CreateUserUseCase:
    return create_user_usecase_factory(user_repository)
