from flask_restx import Namespace, Resource
from flask import request, jsonify, abort, current_app
import jwt

from project.setup.api.models import auth, auth_result
from project.container import user_service

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.expect(auth)
    @api.marshal_with(auth_result, code=200)
    def get(self):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
           user = jwt.decode(token, key=current_app.config['SECRET_KEY'],
                       algorithm=current_app.config['JWT_ALGORITHM'])
        except Exception as error:
            print(error)
            abort(401)

        return jsonify(user)

    @api.expect(auth)
    @api.marshal_with(auth_result, code=200)
    def patch(self):
        data = request.json

        user_info = {
            'name': data.get('name'),
            'surname': data.get('surname'),
            'favorite_genre': data.get('favorite_genre')
        }

        return user_service.update(user_info)


@api.route('password')
class UserPasswordView(Resource):

    @api.expect(auth)
    @api.marshal_with(auth_result, code=200)
    def put(self):
        data = request.json
        email = data.get('email')
        new_password = data.get('new_password')

        return user_service.update_password(email, new_password), 200
