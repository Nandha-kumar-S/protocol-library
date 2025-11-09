from contextlib import contextmanager
import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from db.db_service import DBService

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./protocol_library.db")

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for declarative models
Base = declarative_base()

def init_db() -> None:
    """Initialize the database, creating all tables"""
    Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    """Dependency function to get a database session
    
    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()  # Commit the transaction if no exceptions occurred
    except Exception:
        db.rollback()  # Rollback the transaction if an exception occurred
        raise
    finally:
        db.close()

def get_db_service() -> Generator[DBService, None, None]:
    """Dependency function to get a DBService instance
    
    Yields:
        DBService: Database service instance with ORM operations
    """
    db = SessionLocal()
    try:
        db_service = DBService(db)
        yield db_service
        db.commit()  # Commit the transaction if no exceptions occurred
    except Exception:
        db.rollback()  # Rollback the transaction if an exception occurred
        raise
    finally:
        db.close()


@contextmanager
def get_db_context():
    """Context manager to get a database session"""
    db = SessionLocal()
    try:
        yield db
        db.commit()  # Commit the transaction if no exceptions occurred
    except Exception:
        db.rollback()  # Rollback the transaction if an exception occurred
        raise
    finally:
        db.close()
