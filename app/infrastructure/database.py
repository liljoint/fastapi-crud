from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SQLALCHEMY_DATABASE_URL="sqlite:///./data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

class Base(DeclarativeBase):
    pass

LocalSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

