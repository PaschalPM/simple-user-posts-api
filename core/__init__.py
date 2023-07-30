from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from .config import load_config

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(load_config())
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app, origins='*')
httpauth = HTTPBasicAuth()

import auth.http.middleware 

with app.app_context():
    import users.model
    import posts.model
    db.create_all()
