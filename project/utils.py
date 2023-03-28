import json
from typing import Union
from flask import request, abort, current_app, jsonify
import jwt


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorisation' not in request.headers:
            abort(401)

        data = request.headers['Authorisation']
        token = data.split('Beaver')[-1].strip()

        try:
            user_d = jwt.decode(token, current_app.config['SECRET_KEY'], current_app.config['JWT_ALGORITHM'])
        except Exception as e:
            print('JWT Decode exception', e)
            abort(401)

        func(*args, **kwargs)

        return jsonify(user_d)
    return wrapper()
