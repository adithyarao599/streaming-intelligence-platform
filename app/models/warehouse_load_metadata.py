from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.core.database import Base


class WarehouseLoadMetadata(Base):

    __tablename__ = "warehouse_load_metadata"

    load_id = Column(Integer, primary_key=True)

    table_name = Column(String(100))

    records_loaded = Column(Integer)

    load_timestamp = Column(DateTime, default=datetime.utcnow)

    status = Column(String(50))
