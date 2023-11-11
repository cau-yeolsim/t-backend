from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from t_backend.settings import settings

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
