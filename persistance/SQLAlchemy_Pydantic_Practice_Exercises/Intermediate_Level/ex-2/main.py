from main.ex1 import User, UserSchema, engine

from sqlalchemy.orm import sessionmaker


# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Update user email
def update_user_email(user_id: int, new_email: str):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        session.commit()
        print(f"User {user_id} email updated to {new_email}!")
    else:
        print("User not found!")

if __name__ == "__main__":
    update_user_email(1, "john.doe@example.com")