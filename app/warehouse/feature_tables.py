from sqlalchemy import Column, Float, Integer

from app.core.database import Base


class FactMLFeatures(Base):

    __tablename__ = "fact_ml_features"

    feature_key = Column(Integer, primary_key=True)

    engagement_score = Column(Float)

    trend_score = Column(Float)

    engagement_rate = Column(Float)

    revenue_per_view = Column(Float)
