""" Handles all response for various auth operations """

from users.schema import UserSchema
from werkzeug.security import generate_password_hash
import users.model as UserModel
from core import db
from auth.services.auth import AuthService as Auth

user_schema = UserSchema(exclude=["posts"])


def register_user_handler(valid_user_data: dict):
    """Handles user registration and returns new user data
    as http response
    """
    valid_user_data["password"] = generate_password_hash(
        valid_user_data.get("password")
    )
    valid_user_data.pop("password_confirmation")
    valid_user_data = UserModel.User(**valid_user_data)
    db.session.add(valid_user_data)
    db.session.flush()
    db.session.commit()
    return user_schema.dump(valid_user_data), 200