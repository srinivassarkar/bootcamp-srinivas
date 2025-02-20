from sqlalchemy.orm import sessionmaker
from models_with_posts import User, Post, engine #fix imports  -- error here import from adv/ex-1
from pydantic import BaseModel

# Pydantic schemas
class PostSchema(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True

class UserWithPostsSchema(BaseModel):
    name: str
    email: str
    posts: list[PostSchema]

    class Config:
        from_attributes = True

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Fetch user with posts
def fetch_user_with_posts(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        return UserWithPostsSchema.from_orm(user)
    return None

if __name__ == "__main__":
    user = fetch_user_with_posts(1)
    if user:
        print(user.json())
    else:
        print("User not found!")