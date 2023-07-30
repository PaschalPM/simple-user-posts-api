from pathlib import Path
from datetime import timedelta

BASE_DIR = Path('.').resolve()


class Development:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False