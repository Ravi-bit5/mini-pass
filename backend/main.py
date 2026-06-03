
from app.routes.dashboard import router as dashboard_router
from app.routes.github import router as github_router
from app.routes.deployments import router as deployments_router
from fastapi import FastAPI, Depends

from app.services.auth_dependency import get_current_user
from app.database import engine, Base

from app.models.user import User
from app.models.app import App
from app.models.deployment import Deployment
from app.models.deployment_log import DeploymentLog

from app.routes.auth import router as auth_router
from app.routes.apps import router as apps_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini PaaS"
)

# Routers
app.include_router(auth_router)
app.include_router(apps_router)
app.include_router(deployments_router)
app.include_router(github_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message": "Mini PaaS API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/test")
def test():
    return {
        "ok": True
    }

@app.get("/me")
def me(user=Depends(get_current_user)):
    return {
        "email": user
    }