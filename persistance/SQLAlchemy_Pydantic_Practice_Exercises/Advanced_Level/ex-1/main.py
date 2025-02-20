from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from main.ex1 import Base #This is were models are defined import it in the ex-2 models_with_posts.py

# Post model
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

# Update User model
User.posts = relationship("Post", order_by=Post.id, back_populates="user")

# Create tables
Base.metadata.create_all(engine)