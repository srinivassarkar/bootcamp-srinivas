<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI with SQLAlchemy Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-x: auto;
        }
        .content {
            margin-bottom: 20px;
        }
        .note {
            background-color: #e7f3fe;
            border-left: 6px solid #2196F3;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>FastAPI with SQLAlchemy Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application demonstrates how to create items using SQLAlchemy for database interactions. It allows users to create new items and store them in a SQLite database.</p>
        
        <h3>Why?</h3>
        <p>Using a database to store data is essential for most applications. This example shows how to integrate FastAPI with SQLAlchemy to manage data persistence effectively.</p>
        
        <h3>What?</h3>
        <p>The application provides an endpoint ("/items/") that accepts a request to create a new item, which is then stored in a SQLite database.</p>
        
        <h3>How?</h3>
        <p>The application uses SQLAlchemy to define the database model and manage database sessions. Pydantic models are used to validate incoming data and format responses.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
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
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>