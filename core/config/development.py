from pathlib import Path
from datetime import timedelta

BASE_DIR = Path('.').resolve()


class Development:
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    SESSION_TYPE = "filesystem"
    SESSION_COOKIE_PATH = "/api"
    SECRET_KEY = "pUOE3Xo4AeiqnTkVfSP24qwNbi9GtPqY53p72kNe5_MS7cuavn7kzA"
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False