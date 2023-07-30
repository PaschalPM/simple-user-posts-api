""" API Resource View for User's Post(s) """

from flask.wrappers import Response
from flask import request, abort
from flask_restful import Resource
from ..schema import UserSchema
from posts.schema import PostSchema
from core import db
from ..model import User
from marshmallow import ValidationError
from ..http.handlers.user_posts import get_posts_handler, create_post_handler, update_post_handler, delete_post_handler

user_schema = UserSchema()
post_schema = PostSchema(exclude=['author_id'])
update_post_schema = PostSchema(partial=True, exclude=['author_id'])

class UserPostResource(Resource):
    
    def is_user(self, user_id: str) -> None:
        """ This method checks if a user_id is mapped to a 
            user on the database
        """
        current_user = db.session.get(User, user_id)
        if not current_user:
            abort(400, f"User({user_id}) not found")
        self.current_user = current_user


    def get(self, user_id:str, post_id:str=None) -> Response:
        """ This method handles the API resource view to get 
            a user's single/all posts 
        """
        self.is_user(user_id)
        return get_posts_handler(self.current_user, post_id)
    

    def post(self, user_id: str) -> Response: 
        """ This method handles the API resource view to create 
            a user's post 
        """        
        self.is_user(user_id)
        if not request.is_json:
            abort(400, "Invalid post data. Must be a JSON format")
        
        new_post_data = request.json
        
        try:
            post_schema.load(new_post_data)
            return create_post_handler(self.current_user, new_post_data)

        except ValidationError as err:
            abort(400, err.messages)
        
    def put(self, user_id:str, post_id:str) -> Response:
        """ This method handles the API resource view to update 
            a user's post 
        """
        self.is_user(user_id)
        if not request.is_json:
            abort(400, "Invalid post data. Must be a JSON format")

        update_post_data = request.json
        
        try:
            update_post_schema.load(update_post_data)
            return update_post_handler(post_id, update_post_data)        
        except ValidationError as err:
            abort(400, err.messages)
    
    
    def delete(self, user_id:str, post_id:str) -> Response:
        """ This method handles the API resource view to delete 
            a user's post 
        """
        self.is_user(user_id)
        return delete_post_handler(post_id)