import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usa SQLite se estiver na esteira de CI, ou PostgreSQL por padrão
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:senha@localhost:5432/sgpd_db")

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
