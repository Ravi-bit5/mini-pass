from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.deployment import Deployment
from app.schemas import DeploymentCreate

router = APIRouter()


@router.post("/deployments")
def create_deployment(
    deployment_data: DeploymentCreate,
    db: Session = Depends(get_db)
):
    deployment = Deployment(
        app_name=deployment_data.app_name,
        github_url=deployment_data.github_url,
        status="pending"
    )

    db.add(deployment)
    db.commit()

    return {
        "message": "Deployment created successfully"
    }

@router.get("/deployments")
def get_deployments(
    db: Session = Depends(get_db)
):
    deployments = db.query(Deployment).all()

    return deployments

@router.post("/deployments/{deployment_id}/build")
def build_deployment(
    deployment_id: int,
    db: Session = Depends(get_db)
):
    deployment = db.query(Deployment).filter(
        Deployment.id == deployment_id
    ).first()

    if not deployment:
        return {
            "error": "Deployment not found"
        }

    deployment.status = "running"

    db.commit()

    return {
        "message": "Build completed",
        "status": deployment.status
    }