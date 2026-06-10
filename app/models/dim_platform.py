from sqlalchemy import Column, Integer, String

from app.core.database import Base


class DimPlatform(Base):

    __tablename__ = "dim_platform"

    platform_key = Column(Integer, primary_key=True, autoincrement=True)

    platform_name = Column(String(100), unique=True, nullable=False)
