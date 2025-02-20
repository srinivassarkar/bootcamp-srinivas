from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine('sqlite:///app.db', echo=True)

# SQLAlchemy User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

# Pydantic User schema
class UserSchema(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

# Create tables
Base.metadata.create_all(engine)