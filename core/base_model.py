from . import db
from uuid import uuid4
from datetime import datetime


class BaseModel():
    id = db.Column(db.String(255), nullable=False, primary_key=True, default=lambda:str(uuid4()))
    
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
