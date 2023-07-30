from core.base_model import BaseModel
from core import db
from posts.model import Post

class User(db.Model, BaseModel):
    __tablename__ = "users"
    
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False) 
    
    posts = db.relationship(Post, back_populates="author", cascade="all, delete, delete-orphan", lazy=True)