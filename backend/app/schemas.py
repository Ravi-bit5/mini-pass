from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class AppCreate(BaseModel):
    name: str

class DeploymentCreate(BaseModel):
    app_name: str
    github_url: str