from sqlalchemy import Column, Integer, String

from app.database import Base


class Deployment(Base):
    __tablename__ = "deployments"

    id = Column(Integer, primary_key=True, index=True)

    app_name = Column(String)

    github_url = Column(String)

    status = Column(String)