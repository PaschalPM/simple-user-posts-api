from flask import abort
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

def exception_handler(err):
    ''' Handles all http errors regarding any auth operation '''

    if isinstance(err, ValidationError):
        abort(400, err.messages)

    elif isinstance(err, IntegrityError):
        if (str(err).__contains__('UNIQUE')):
            if (str(err).__contains__('users.username')):
                abort(400, "Username already taken.")
            elif (str(err).__contains__('users.email')):
                abort(400, "Email already exists.")