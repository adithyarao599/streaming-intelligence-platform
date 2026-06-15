from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.config.settings import settings

required_settings = {
    "POSTGRES_USER": settings.POSTGRES_USER,
    "POSTGRES_PASSWORD": settings.POSTGRES_PASSWORD,
    "POSTGRES_DB": settings.POSTGRES_DB,
    "POSTGRES_HOST": settings.POSTGRES_HOST,
    "POSTGRES_PORT": settings.POSTGRES_PORT,
}

missing = [k for k, v in required_settings.items() if not v]

if missing:
    raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

DATABASE_URL = (
    f"postgresql://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
)

Base = declarative_base()
