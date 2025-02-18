from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional  

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI application
app = FastAPI()

# Pydantic model for item creation
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

# Pydantic model for item response
class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True  

@app.post("/items/", response_model=ItemResponse)  
def create_item(item: ItemCreate):
    db_item = Item(**item.dict())
    db = SessionLocal()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item  