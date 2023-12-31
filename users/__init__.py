from flask import Blueprint
from flask_restful import Api
from .views.users import UserResource
from .views.user_posts import UserPostResource
from auth.http.middleware import is_user_loggedin

users_bp = Blueprint("users", __name__, url_prefix="/api")
users_bp.before_request(is_user_loggedin)
users_api = Api(users_bp, '/users')
users_api.add_resource(UserResource, "/", "/<string:id>")

user_posts_api = Api(users_bp, '/users/<string:user_id>')
user_posts_api.add_resource(UserPostResource, "/posts", "/posts/<string:post_id>")