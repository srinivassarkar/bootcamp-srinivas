<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Python ORM Notes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
    </style>
</head>
<body>
    <h1>My Notes on Advanced Python Usage: ORM with SQLAlchemy + Pydantic</h1>
    <p>Coming from a MERN stack background, I’m diving into Python and ORMs. Here’s what I’ve learned so far, written as my personal notes!</p>

    <h2>What is an ORM?</h2>
    <p>ORM stands for <strong>Object-Relational Mapping</strong>. It’s a way to work with relational databases (like SQLite) using Python objects instead of raw SQL. In MERN, I used MongoDB (NoSQL) with JSON-like documents, but relational DBs use tables and rows, so ORM makes that easier.</p>
    <ul>
        <li><strong>How it works</strong>: Maps database tables to Python classes and rows to objects.</li>
        <li><strong>Example</strong>: Instead of <code>SELECT * FROM users WHERE id = 1</code>, I’d write <code>User.query.get(1)</code>.</li>
    </ul>

    <h3>Why Do We Need ORM?</h3>
    <p>In MERN, I didn’t need this because MongoDB’s documents matched JavaScript objects naturally. But with relational DBs, ORM is a game-changer:</p>
    <ol>
        <li><strong>Abstraction</strong>: No need to write messy SQL—ORM does it for me.</li>
        <li><strong>Productivity</strong>: Faster to code with Python classes than SQL strings.</li>
        <li><strong>Maintainability</strong>: Cleaner code, easier to update.</li>
        <li><strong>Flexibility</strong>: Switch databases (e.g., SQLite to MySQL) with little rework.</li>
        <li><strong>Security</strong>: Prevents SQL injection by default.</li>
    </ol>

    <h2>SQLAlchemy + Pydantic: My New Tools</h2>
    <p>These replace parts of my MERN stack:</p>
    <ul>
        <li><strong>SQLAlchemy</strong>: Like Mongoose but for Python and relational DBs. It’s my ORM.</li>
        <li><strong>Pydantic</strong>: Like TypeScript for validating data—ensures my objects have the right shape.</li>
    </ul>

    <h3>SQLAlchemy</h3>
    <p>It’s a Python library that lets me define models as classes and query them. Here’s a simple example:</p>
    <pre><code>from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
</code></pre>

    <h3>Pydantic</h3>
    <p>Validates my data and gives me typed objects. Super useful for APIs or DB results:</p>
    <pre><code>from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # Works with SQLAlchemy
</code></pre>

    <h3>Together</h3>
    <p>SQLAlchemy talks to the DB, Pydantic validates the data. Perfect combo for something like FastAPI (my Express.js replacement).</p>

    <h2>Setting Up with SQLite</h2>
    <p>I’m using SQLite since it’s file-based and easy—no server setup like PostgreSQL. Here’s how I got started:</p>

    <h3>1. Python Environment</h3>
    <pre><code>python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install sqlalchemy pydantic
</code></pre>
    <p>SQLite is built into Python, so no extra driver needed!</p>

    <h3>2. My Example Code</h3>
    <p>File: <code>main.py</code></p>
    <pre><code>from sqlalchemy import create_engine, Column, Integer, String
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
</code></pre>
    <p>Run it: <code>python main.py</code>. Creates <code>mydb.db</code> file with my data!</p>

    <h2>Visualizing DB - ORM - Python</h2>
    <p>This image sums it up—how my DB tables connect to Python code through the ORM:</p>
    <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*UkOqM_a_agYwUOoV" alt="DB - ORM - Python Code Diagram">

    <h2>MERN vs. This</h2>
    <ul>
        <li><strong>MongoDB → SQLite</strong>: Documents to tables.</li>
        <li><strong>Mongoose → SQLAlchemy</strong>: Schema in JS to Python ORM.</li>
        <li><strong>JSON → Pydantic</strong>: Raw JSON to validated Python objects.</li>
        <li><strong>Express → FastAPI</strong>: Backend swap (future goal).</li>
    </ul>



    <p><em>Last updated: February 21, 2025: Created By GROK AI v3</em></p>
</body>
</html>