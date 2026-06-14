from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.core.database import Base


class MLMetadata(Base):

    __tablename__ = "ml_metadata"

    model_id = Column(Integer, primary_key=True)

    model_name = Column(String(100))

    accuracy = Column(Float)

    training_date = Column(DateTime, default=datetime.utcnow)
