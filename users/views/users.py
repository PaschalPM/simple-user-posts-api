''' API Views for users '''

from flask import request, abort
from flask_restful import Resource
from users.http.handlers.users import get_users_handler, delete_user_handler, update_user_handler
from users.schema import UserSchema
from marshmallow import ValidationError


class UserResource(Resource):
    def get(self, id=None):
        ''' Gets single or all users'''

        return get_users_handler(id)
 
        
    def delete(self, id):
        ''' Deletes a user by id'''
    
        return delete_user_handler(id)
  
  
    def put(self, id):
        ''' Updates a user's property/properties by id'''

        user_update_schema = UserSchema(partial=True, exclude=["password_confirmation", "id"]) 
        user_data = request.json
        
        if not user_data:
            abort(400, "Invalid request data. Ensure it is a JSON type")
            
        try:
            user_inst = user_update_schema.load(user_data)
            return update_user_handler(id, user_inst)

        except ValidationError as err:
            abort(400, err.messages)