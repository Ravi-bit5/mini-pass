from fastapi import FastAPI

from app.database import engine, Base
from app.models.user import User
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini PaaS"
)

app.include_router(auth_router)

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
    return {"ok": True}