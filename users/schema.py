from marshmallow import fields, validate
from core import ma
from posts.schema import PostSchema


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ["id", "username", "password", "email", "password_confirmation", "posts"]

    username = fields.String(required=True, validate=validate.Length(min=1, max=50))    
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=8, max=50, error="Password must be atleast 8 characters long"))
    password_confirmation = fields.String(required=True, load_only=True)
    posts = fields.Nested(PostSchema, many=True, exclude=['author_id'])