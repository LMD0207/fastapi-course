from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Usage sqlite
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# engine = create_engine(
#   SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
# )

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
