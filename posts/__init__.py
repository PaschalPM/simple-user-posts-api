from flask_restful import Api
from flask import Blueprint
from .views import PostResource


posts_bp = Blueprint("posts", __name__, url_prefix="/api")
posts_api = Api(posts_bp, "/posts")
posts_api.add_resource(PostResource, '/', '/<string:id>')