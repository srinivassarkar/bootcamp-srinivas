from sqlalchemy.orm import sessionmaker
from models import User, engine #fix imports  -- error here 

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Bulk insert users
def bulk_insert_users(users_data: list[dict]):
    try:
        session.begin()
        for user_data in users_data:
            user = User(name=user_data['name'], email=user_data['email'])
            session.add(user)
        session.commit()
        print("Bulk insert successful!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

if __name__ == "__main__":
    users_data = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]
    bulk_insert_users(users_data)