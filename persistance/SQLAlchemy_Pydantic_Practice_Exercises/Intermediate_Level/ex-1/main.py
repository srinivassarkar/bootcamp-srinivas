from sqlalchemy.orm import sessionmaker
from main.ex1 import User, UserSchema, engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Filter user by email
def get_user_by_email(email: str):
    user = session.query(User).filter(User.email == email).first()
    if user:
        return UserSchema.from_orm(user)
    return None

if __name__ == "__main__":
    user = get_user_by_email("john@example.com")
    if user:
        print(user.json())
    else:
        print("User not found!")