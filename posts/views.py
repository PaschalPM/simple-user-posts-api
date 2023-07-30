""" Post API Resource View """

from flask.wrappers import Response
from flask_restful import Resource
from core import db
from .model import Post
from .schema import PostSchema

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

class PostResource(Resource):
    def get(self, id=None) -> Response:
        ''' This methods handles the API resource view that returns
            single/all posts
        '''
        if id:
            selected_post = db.session.get(Post, id)
            return post_schema.dump(selected_post), 200
        
        query = db.select(Post).order_by(Post.created_at.desc())
        posts = db.session.scalars(query)
        return posts_schema.dump(posts), 200
        