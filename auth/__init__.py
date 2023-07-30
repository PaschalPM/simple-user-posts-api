from flask import Blueprint
from flask_restful import Api
from .views import AuthResource
from .http.middleware import is_user_loggedin

auth_bp = Blueprint("auth", __name__, url_prefix="/api")
auth_bp.before_request(is_user_loggedin)
auth_api = Api(auth_bp, "/auth")
auth_api.add_resource(AuthResource, "/register", "/login", "/logout")