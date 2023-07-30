''' Post Model '''

from core.base_model import BaseModel
from core import db
from slugify import slugify


class Post(db.Model, BaseModel):
    __tablename__ = "posts"
    
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    author_id = db.Column(db.ForeignKey("users.id"))
    
    author = db.relationship("User", back_populates="posts")
    
    @property
    def slug(self):
        """ Creates a slug property 
        """
        separator = ":"
        return f"{slugify(self.title)}{separator}{self.id}"