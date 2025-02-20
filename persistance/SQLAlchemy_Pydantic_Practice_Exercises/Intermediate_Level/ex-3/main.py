from main.ex1 import User, UserSchema, engine

from sqlalchemy.orm import sessionmaker

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Delete user
def delete_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user_id} deleted successfully!")
    else:
        print("User not found!")

if __name__ == "__main__":
    delete_user(1)