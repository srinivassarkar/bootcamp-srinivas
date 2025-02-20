from sqlalchemy.orm import sessionmaker
from ex1.main import User, UserSchema, engine, SessionLocal  

# Create session
session = SessionLocal()

# Insert user
def insert_user(name: str, email: str):
    user_data = UserSchema(name=name, email=email)  # Validate with Pydantic
    user = User(name=user_data.name, email=user_data.email)
    session.add(user)
    session.commit()
    print(f"User {name} inserted successfully!")

if __name__ == "__main__":
    insert_user("John Doe", "john@example.com")
