""" API View for auth operations """

from flask import request, abort, Response
from flask_restful import Resource
from .http.handlers.auth import register_user_handler
from users.schema import UserSchema
from .http.handlers.exceptions import exception_handler
from marshmallow import ValidationError

user_register_schema = UserSchema()
user_login_schema = UserSchema(partial=True, exclude=["password_confirmation"])


class AuthResource(Resource):
    def __init__(self) -> None:
        """Runs before every auth operation"""
        if not request.is_json:
            abort(400, "Invalid data format. Payload must be JSON")
        self.user_payload = request.json

    def post(self) -> Response:
        """This method handles auth registration

        Return: HTTP Response
        """
        new_user = self.user_payload
        try:
            if new_user.get("password") != new_user.get("password_confirmation"):
                raise ValidationError(
                    "Password does not match", field_name="password_confirmation"
                )
            user_register_schema.load(new_user)
            return register_user_handler(new_user)

        except Exception as err:
            return exception_handler(err)
