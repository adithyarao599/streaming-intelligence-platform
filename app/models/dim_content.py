from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String

from app.core.database import Base


class DimContent(Base):

    __tablename__ = "dim_content"

    content_key = Column(Integer, primary_key=True, autoincrement=True)

    content_id = Column(String(100), nullable=False)

    content_name = Column(String(255), nullable=False)

    content_type = Column(String(50), nullable=False)

    release_date = Column(Date)

    duration_minutes = Column(Float)

    genre_key = Column(Integer, ForeignKey("dim_genre.genre_key"))
