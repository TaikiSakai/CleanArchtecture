from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.presentation.schemas.user import UserCreateSchema, UserSchema
from src.usecases.user.create_user_usecase import CreateUserUseCase
from src.usecases.user.get_user_usecase import GetUserUseCase
from src.infrastructures.di.user import get_get_user_usecase
from src.infrastructures.di.user import get_create_user_usecase
from src.entities.exceptions.user import UserNotFoundError

router = APIRouter(tags=["user"])

@router.get("/user/{user_id}")
def get_user(
    user_id: int,
    usecase: GetUserUseCase = Depends(get_get_user_usecase),
) -> UserSchema:
    try:
        user = usecase.execute(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return UserSchema.from_entity(user)


@router.get("/users", response_model=list[UserSchema])
def get_users():
    pass


@router.post("/user/new")
def create_user(
    data: UserCreateSchema,
    usecase: CreateUserUseCase = Depends(get_create_user_usecase),
    db: Session = Depends(get_db)
) -> UserSchema:
    try:
        with db.begin():
            user = usecase.execute(
                email=data.email,
                user_name=data.user_name,
                is_active=data.is_active,
                role=data.role
            )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return UserSchema.from_entity(user)
