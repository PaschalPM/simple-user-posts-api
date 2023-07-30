from core import app, httpauth
from auth import auth_bp
from users import users_bp
from posts import posts_bp


app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)


if __name__ == "__main__":
    app.run()