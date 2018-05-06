from flask import jsonify, request, g, current_app, url_for
from flask_restful import Resource
from app.api import api
from app.models.User import User


@api.resource('/users')
class UserList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        pagination = User.query.pagination(
            page,
            per_page=current_app.config.get('USER_PER_PAGE'),
            error_out=False
        )
        users = pagination.items
        prev = None
        if pagination.has_prev:
            prev = url_for('api.get_users', page=page - 1)
        next = None
        if pagination.has_next:
            next = url_for('api.get_users', page=page + 1)
        return jsonify({
            'users': [],
            'prev': prev,
            'next': next,
            'total': pagination.total
        })

    def post(self):
        data = request.get_json(force=True)
        return data


@api.resource('/users/<int:id>')
class UserItem(Resource):
    def get(self, id):
        # user = User.
        return id

    def patch(self):
        return {}, 200

    def delete(self):
        return {}, 200


@api.resource('/users/<int:id>/status')
class UserStatus(Resource):
    def patch(self, id):
        return {}
