from flask import request as req
from ..services.auth import AuthService as Auth

EXCLUDED_METHODS = ['GET']
EXCLUDED_PATHS = ['/api/auth/register', '/api/auth/login']

def is_user_loggedin():
    """ This middleware functions checks if user is logged in 
    """
    if not req.method in EXCLUDED_METHODS and not req.path in EXCLUDED_PATHS:
        if not Auth.current_user():
            return {"message": "User is unauthorized"}, 401        