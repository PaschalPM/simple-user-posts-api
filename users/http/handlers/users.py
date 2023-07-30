""" HTTP Handler for User's API View """

from core import db
from users.model import User
from users.schema import UserSchema
from werkzeug.security import generate_password_hash

user_schema = UserSchema(exclude=['password_confirmation'])
users_schema = UserSchema(many=True, exclude=['password_confirmation', 'posts'])


def get_users_handler(id:str = None):
    """  This handler gets single/all user(s) 
    """
    if id:
        user = db.session.get(User, id)
        return user_schema.dump(user), 200
    
    query = db.select(User).order_by(User.created_at.desc())
    users = db.session.scalars(query)
    return users_schema.dump(users), 200


def delete_user_handler(id):
    """  This handler deletes a single user 
    """
    user = db.session.get(User, id)
    db.session.delete(user)
    db.session.commit()
    return "", 204


def update_user_handler(id, valid_data):
    """ This handler updates a single user using validated user 
        data from its view
    """
    if valid_data.get("password"):
        valid_data["password"] = generate_password_hash(valid_data.get("password"))

    user = db.session.get(User, id)
    [setattr(user, key, val) for key, val in valid_data.items()]
    db.session.flush()
    db.session.commit()
    return {"message": "User updated successfully"}, 200