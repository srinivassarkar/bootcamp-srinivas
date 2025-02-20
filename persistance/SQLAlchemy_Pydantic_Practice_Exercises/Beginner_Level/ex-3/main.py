from sqlalchemy.orm import sessionmaker
from ex1.main import User, UserSchema, engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Fetch users
def fetch_users():
    users = session.query(User).all()
    return [UserSchema.from_orm(user) for user in users]

if __name__ == "__main__":
    users = fetch_users()
    for user in users:
        print(user.json())