from flask_restful import Api
from flask import Blueprint
from .views import PostResource
from auth.http.middleware import is_user_loggedin


posts_bp = Blueprint("posts", __name__, url_prefix="/api")
posts_bp.before_request(is_user_loggedin)
posts_api = Api(posts_bp, "/posts")
posts_api.add_resource(PostResource, '/', '/<string:id>')