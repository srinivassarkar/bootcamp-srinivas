# My Notes on Advanced Python Usage: ORM with SQLAlchemy + Pydantic

Coming from a MERN stack background, I’m diving into Python and ORMs. Here’s what I’ve learned so far, written as my personal notes!

## What is an ORM?

ORM stands for **Object-Relational Mapping**. It’s a way to work with relational databases (like SQLite) using Python objects instead of raw SQL. In MERN, I used MongoDB (NoSQL) with JSON-like documents, but relational DBs use tables and rows, so ORM makes that easier.

*   **How it works**: Maps database tables to Python classes and rows to objects.
*   **Example**: Instead of `SELECT * FROM users WHERE id = 1`, I’d write `User.query.get(1)`.

### Why Do We Need ORM?

In MERN, I didn’t need this because MongoDB’s documents matched JavaScript objects naturally. But with relational DBs, ORM is a game-changer:

1.  **Abstraction**: No need to write messy SQL—ORM does it for me.
2.  **Productivity**: Faster to code with Python classes than SQL strings.
3.  **Maintainability**: Cleaner code, easier to update.
4.  **Flexibility**: Switch databases (e.g., SQLite to MySQL) with little rework.
5.  **Security**: Prevents SQL injection by default.

## SQLAlchemy + Pydantic: My New Tools

These replace parts of my MERN stack:

*   **SQLAlchemy**: Like Mongoose but for Python and relational DBs. It’s my ORM.
*   **Pydantic**: Like TypeScript for validating data—ensures my objects have the right shape.

### SQLAlchemy

It’s a Python library that lets me define models as classes and query them. Here’s a simple example:

    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)

### Pydantic

Validates my data and gives me typed objects. Super useful for APIs or DB results:

    from pydantic import BaseModel

    class UserSchema(BaseModel):
        id: int
        name: str
        email: str

        class Config:
            orm_mode = True  # Works with SQLAlchemy

### Together

SQLAlchemy talks to the DB, Pydantic validates the data. Perfect combo for something like FastAPI (my Express.js replacement).

## Setting Up with SQLite

I’m using SQLite since it’s file-based and easy—no server setup like PostgreSQL. Here’s how I got started:

### 1\. Python Environment

    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install sqlalchemy pydantic

SQLite is built into Python, so no extra driver needed!

### 2\. My Example Code

File: `main.py`

    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from pydantic import BaseModel

    # SQLite connection (file-based DB)
    engine = create_engine("sqlite:///mydb.db")
    Base = declarative_base()

    # SQLAlchemy Model
    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)

    # Pydantic Model
    class UserSchema(BaseModel):
        id: int
        name: str
        email: str

        class Config:
            orm_mode = True

    # Create the table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a user
    new_user = User(name="John Doe", email="john@example.com")
    session.add(new_user)
    session.commit()

    # Query and validate
    user = session.query(User).first()
    user_pydantic = UserSchema.from_orm(user)
    print(user_pydantic.dict())  # {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}

Run it: `python main.py`. Creates `mydb.db` file with my data!

## Visualizing DB - ORM - Python

This image sums it up—how my DB tables connect to Python code through the ORM:

![DB - ORM - Python Code Diagram](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*UkOqM_a_agYwUOoV)

## MERN vs. This

*   **MongoDB → SQLite**: Documents to tables.
*   **Mongoose → SQLAlchemy**: Schema in JS to Python ORM.
*   **JSON → Pydantic**: Raw JSON to validated Python objects.
*   **Express → FastAPI**: Backend swap (future goal).

_Last updated: February 21, 2025: Created By GROK AI v3_