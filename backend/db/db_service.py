from typing import Any, Dict, List, Optional, Type, TypeVar, Union
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.sql import Select

T = TypeVar('T')

class DBService:
    def __init__(self, session: Session):
        self._session = session

    def get(self, model: Type[T], **conditions) -> List[T]:
        """
        Get all records of a model that match the given conditions
        
        Args:
            model: SQLAlchemy model class
            **conditions: Filter conditions as keyword arguments
        
        Returns:
            List of model instances
        
        Example:
            users = db.get(User, role="admin", is_active=True)
        """
        query = select(model).filter_by(**conditions)
        return list(self._session.scalars(query).all())

    def get_one(self, model: Type[T], **conditions) -> Optional[T]:
        """
        Get single record of a model that matches the given conditions
        
        Args:
            model: SQLAlchemy model class
            **conditions: Filter conditions as keyword arguments
        
        Returns:
            Single model instance or None if not found
        
        Example:
            user = db.get_one(User, email="user@example.com")
        """
        query = select(model).filter_by(**conditions)
        return self._session.scalars(query).first()

    def add(self, instance: T) -> T:
        """
        Add a new record to the database
        
        Args:
            instance: Model instance to add
        
        Returns:
            Added model instance
        
        Example:
            new_user = User(name="John")
            db.add(new_user)
            db.commit()  # Remember to commit when done with all operations
        """
        self._session.add(instance)
        return instance

    def add_all(self, instances: List[T]) -> List[T]:
        """
        Add multiple records to the database
        
        Args:
            instances: List of model instances to add
        
        Returns:
            List of added model instances
        
        Example:
            users = [User(name="John"), User(name="Jane")]
            db.add_all(users)
            db.commit()  # Remember to commit when done with all operations
        """
        self._session.add_all(instances)
        return instances

    def update(self, model: Type[T], values: Dict[str, Any], **conditions) -> int:
        """
        Update records that match the conditions with given values
        
        Args:
            model: SQLAlchemy model class
            values: Dictionary of column names and values to update
            **conditions: Filter conditions as keyword arguments
        
        Returns:
            Number of records updated
        
        Example:
            count = db.update(User, {"is_active": False}, role="guest")
            db.commit()  # Remember to commit when done with all operations
        """
        stmt = (
            update(model)
            .filter_by(**conditions)
            .values(**values)
            .returning(model)
        )
        result = self._session.execute(stmt)
        return result

    def delete(self, model: Type[T], **conditions) -> int:
        """
        Delete records that match the conditions
        
        Args:
            model: SQLAlchemy model class
            **conditions: Filter conditions as keyword arguments
        
        Returns:
            Number of records deleted
        
        Example:
            count = db.delete(User, is_active=False)
            db.commit()  # Remember to commit when done with all operations
        """
        stmt = delete(model).filter_by(**conditions)
        result = self._session.execute(stmt)
        return result.rowcount

    def execute(self, query: Union[str, Select]) -> Any:
        """
        Execute a raw SQL query or SQLAlchemy select statement
        
        Args:
            query: SQL query string or SQLAlchemy select statement
        
        Returns:
            Query result
        
        Example:
            result = db.execute(select(User).where(User.age > 18))
        """
        result = self._session.execute(query)
        return result

    def commit(self) -> None:
        """
        Commit the current transaction
        """
        self._session.commit()

    def rollback(self) -> None:
        """
        Rollback the current transaction
        """
        self._session.rollback()

    def close(self) -> None:
        """
        Close the session
        """
        self._session.close()
