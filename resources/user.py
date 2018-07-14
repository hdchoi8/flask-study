from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource) :

    parse = reqparse.RequestParser()
    parse.add_argument('username', type=str, required= True, help='This field can not be blanked')
    parse.add_argument('password', type=str, required=True, help='This field can not be blanked')

    def post(self):
        data = UserRegister.parse.parse_args()
        user = UserModel.query.filter_by(username=data['username']).first()
        if user:
            name = data['username']
            return {'message': f'{name} already exists'}

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {'message': 'user successfully created'}
