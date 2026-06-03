from sqlalchemy import Column, Integer, String

from app.database import Base


class DeploymentLog(Base):
    __tablename__ = "deployment_logs"

    id = Column(Integer, primary_key=True, index=True)

    deployment_id = Column(Integer)

    message = Column(String)