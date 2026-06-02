from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas import UserCreate
from app.services.security import hash_password

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