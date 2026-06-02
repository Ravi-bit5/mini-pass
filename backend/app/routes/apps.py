from app.services.auth_dependency import get_current_user

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.app import App
from app.schemas import AppCreate

router = APIRouter()


@router.post("/apps")
def create_app(
    app_data: AppCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    app = App(
        name=app_data.name,
        owner_email=current_user,
        image_name="none"
    )

    db.add(app)
    db.commit()

    return {
        "message": "App created successfully"
    }



@router.get("/apps")
def get_apps(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    apps = db.query(App).filter(
        App.owner_email == current_user
    ).all()

    return apps