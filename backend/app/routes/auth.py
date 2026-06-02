from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

from app.schemas import UserCreate, UserLogin

from app.services.security import (
    hash_password,
    verify_password
)

from app.services.jwt_service import (
    create_access_token
)

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    print("REGISTER HIT")

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    print("USER CREATED")

    db.add(new_user)

    print("ADDED TO DB")

    db.commit()

    print("COMMIT SUCCESS")

    return {
        "message": "User registered successfully"
    }
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:
        return {
            "message": "Invalid email"
        }

    if not verify_password(
        user.password,
        db_user.password
    ):
        return {
            "message": "Invalid password"
        }

    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }