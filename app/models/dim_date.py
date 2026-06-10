from sqlalchemy import Column, Date, Integer

from app.core.database import Base


class DimDate(Base):

    __tablename__ = "dim_date"

    date_key = Column(Integer, primary_key=True)

    full_date = Column(Date, nullable=False)

    day = Column(Integer)

    month = Column(Integer)

    quarter = Column(Integer)

    year = Column(Integer)

    week = Column(Integer)
