from core import httpauth
from ..services.auth import AuthService as Auth


@httpauth.verify_password
def verify_password(username_or_email, password):
    """Verified User's credentials"""
    
    return Auth.confirm_creds(username_or_email, password)


@httpauth.error_handler
def unauthorized():
    """Throw and return error in JSON format"""
    
    return {'error': 'Unauthorized access'}, 401