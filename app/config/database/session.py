from sqlalchemy import Engine
from sqlmodel import create_engine
from app.config.settings import DB_URL, DB_NAME

engine = create_engine(
    url=DB_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=0,
)
