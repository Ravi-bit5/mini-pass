from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.deployment import Deployment
from app.schemas import DeploymentCreate
from app.models.deployment_log import DeploymentLog

router = APIRouter()


@router.post("/deployments")
def create_deployment(
    deployment_data: DeploymentCreate,
    db: Session = Depends(get_db)
):

    if not deployment_data.github_url.startswith("https://github.com/"):
        return {
            "error": "Invalid GitHub repository URL"
        }

    deployment = Deployment(
        app_name=deployment_data.app_name.strip(),
        github_url=deployment_data.github_url.strip(),
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

@router.post("/deployments/{deployment_id}/generate-logs")
def generate_logs(
    deployment_id: int,
    db: Session = Depends(get_db)
):
    logs = [
        "Cloning repository...",
        "Installing dependencies...",
        "Building application...",
        "Starting application...",
        "Application running..."
    ]

    for message in logs:
        log = DeploymentLog(
            deployment_id=deployment_id,
            message=message
        )
        db.add(log)

    db.commit()

    return {
        "message": "Logs generated"
    }

@router.get("/deployments/{deployment_id}/logs")
def get_logs(
    deployment_id: int,
    db: Session = Depends(get_db)
):
    logs = db.query(DeploymentLog).filter(
        DeploymentLog.deployment_id == deployment_id
    ).all()

    return logs