from sqlalchemy import Column, Integer, String

from app.core.database import Base


class DimCountry(Base):

    __tablename__ = "dim_country"

    country_key = Column(Integer, primary_key=True, autoincrement=True)

    country_code = Column(String(10), nullable=False, unique=True)

    country_name = Column(String(100), nullable=False)
