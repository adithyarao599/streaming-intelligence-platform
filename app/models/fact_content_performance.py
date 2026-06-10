from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, Numeric

from app.core.database import Base


class FactContentPerformance(Base):

    __tablename__ = "fact_content_performance"

    performance_key = Column(BigInteger, primary_key=True, autoincrement=True)

    date_key = Column(Integer, ForeignKey("dim_date.date_key"))

    content_key = Column(Integer, ForeignKey("dim_content.content_key"))

    artist_key = Column(Integer, ForeignKey("dim_artist.artist_key"))

    genre_key = Column(Integer, ForeignKey("dim_genre.genre_key"))

    platform_key = Column(Integer, ForeignKey("dim_platform.platform_key"))

    country_key = Column(Integer, ForeignKey("dim_country.country_key"))

    views = Column(BigInteger)

    streams = Column(BigInteger)

    likes = Column(BigInteger)

    comments = Column(BigInteger)

    shares = Column(BigInteger)

    watch_hours = Column(Float)

    revenue = Column(Numeric(18, 2))

    trend_score = Column(Float)
