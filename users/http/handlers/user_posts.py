"""" HTTP Handler for User's Post Views """

from flask import Response
from core import db
from posts.model import Post
from posts.schema import PostSchema
from users.model import User

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


def get_posts_handler(current_user: User, post_id: str) -> Response:
    """ The handler gets the current user's single/all posts 
    """
    if post_id:
        selected_post = db.session.get(Post, post_id)
        return post_schema.dump(selected_post), 200
    
    query = db.select(Post).filter_by(author=current_user).order_by(Post.created_at.desc())
    posts = db.session.scalars(query)
    return posts_schema.dump(posts), 200


def create_post_handler(current_user:User, valid_post_data: dict) -> Response:
    """ This handler creates a new post for the current user 
    """
    new_post = Post(**valid_post_data, author=current_user)
    db.session.add(new_post)
    db.session.commit()
    return {"message": "Post created successfully"}, 201


def update_post_handler(post_id:str, valid_post_data: dict) -> Response:
    """ This handler updates a post for the current user 
    """
    selected_post = db.session.get(Post, post_id)
    [setattr(selected_post, key, val) for key, val in valid_post_data.items()]
    db.session.commit()
    return post_schema.dump(selected_post), 200


def delete_post_handler(post_id:str) -> Response:
    """ This handler deletes a post for the current user 
    """
    selected_post = db.session.get(Post, post_id)
    db.session.delete(selected_post)
    db.session.commit()
    return "", 204