from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)

# Depend
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
