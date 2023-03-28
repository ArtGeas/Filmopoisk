from flask_restx import Namespace, Resource
from flask import request, jsonify, abort, current_app
import jwt

from project.setup.api.models import auth, auth_result
from project.container import user_service
from ...utils import auth_required

api = Namespace('user')


@api.route('/')
class UserView(Resource):

    @auth_required
    def get(self):
        pass

    @auth_required
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

    @auth_required
    def put(self):
        data = request.json
        email = data.get('email')
        new_password = data.get('new_password')

        return user_service.update_password(email, new_password), 200
