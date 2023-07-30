from flask import session
from core import db
# from users.model import User
from werkzeug.security import check_password_hash
from sqlalchemy import or_


class AuthService:
    """ This class is responsible for major auth operations """

    @classmethod
    def login(cls, username:str, email:str, password:str) -> None:
        """ Logs a user in a creates a session """
        from users.model import User
        query = db.select(User).where(or_(User.username == username, User.email == email))
        current_user = db.session.scalar(query)
        is_auth = False
        if current_user:
            if check_password_hash(current_user.password, password):
                session["user"] = current_user
                is_auth = True
        return current_user if is_auth else None
    
    @classmethod
    def current_user(cls):
        """ Get logged in/ current user """
        return session.get("user", None)
    
    
    @classmethod
    def logout(cls):
        """ Logout user """
        return session.pop("user", None)
        