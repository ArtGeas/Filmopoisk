from flask_restx import Namespace, Resource
from flask import request

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser, status_page_parser

api = Namespace('users')


@api.route('/')
class UsersViews(Resource):
    @api.expect(status_page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all users.
        """
        return user_service.get_all(**page_parser.parse_args())


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        Get user by id.
        """
        return user_service.get_one(user_id)

    @api.marshal_with(user, code=200, description='OK')
    def patch(self, user_id: int):

        return user_service.update(user_id)


@api.route('/password/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    @api.marshal_with(user, code=200, description='OK')
    def put(self):

        data = request.json
        email = data.get('email')
        new_password = data.get('new_password')
        return user_service.update_password(email, new_password)
