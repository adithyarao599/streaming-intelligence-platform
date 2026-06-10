from sqlalchemy import Column, Integer, String

from app.core.database import Base


class DimGenre(Base):

    __tablename__ = "dim_genre"

    genre_key = Column(Integer, primary_key=True, autoincrement=True)

    genre_name = Column(String(100), unique=True, nullable=False)
