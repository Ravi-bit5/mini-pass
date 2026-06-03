from fastapi import APIRouter
from sqlalchemy import func

from app.database import SessionLocal
from app.models.app import App
from app.models.deployment import Deployment

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    db = SessionLocal()

    apps_count = db.query(App).count()

    deployments_count = db.query(Deployment).count()

    running_count = db.query(Deployment).filter(
        Deployment.status == "running"
    ).count()

    return {
        "apps": apps_count,
        "deployments": deployments_count,
        "running_deployments": running_count,
        "repositories": 3
    }