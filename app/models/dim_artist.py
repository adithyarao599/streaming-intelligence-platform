from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

from app.core.database import Base


class DimArtist(Base):

    __tablename__ = "dim_artist"

    artist_key = Column(Integer, primary_key=True, autoincrement=True)

    artist_id = Column(String(100), nullable=False)

    artist_name = Column(String(255), nullable=False)

    country_key = Column(Integer, ForeignKey("dim_country.country_key"))

    active_flag = Column(Boolean, default=True)

    effective_date = Column(Date)

    end_date = Column(Date)
