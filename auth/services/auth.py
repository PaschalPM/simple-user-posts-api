from flask import request as req
from core import db
from werkzeug.security import check_password_hash
from sqlalchemy import or_
from base64 import b64decode


class AuthService:
    """This class is responsible for major auth operations"""

    @classmethod
    def confirm_creds(cls, username_or_email: str, password: str) -> None:
        """Verify user against the database"""
        from users.model import User

        query = db.select(User).where(
            or_(User.username == username_or_email, User.email == username_or_email)
        )
        current_user = db.session.scalar(query)
        if current_user:
            if check_password_hash(current_user.password, password):
                return True
            return False
        return False