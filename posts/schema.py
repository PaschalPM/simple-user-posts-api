""" Post Schema """

from core import ma
from marshmallow import fields, validate
from .model import Post

class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "slug", "created_at", "author_id"]
        ordered = True
        
    id = fields.String(required=True, dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=3, max=100))
    body = fields.String(required=True, validate=validate.Length(min=10, max=1000))
    author_id = fields.String(required=True, validate=validate.Length(equal=36))
    slug = fields.String(required=True, dump_only=True)
    created_at = fields.String(required=True, dump_only=True)