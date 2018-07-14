from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(name, password) :
    user = UserModel.find_by_username(name)

    if user and safe_str_cmp( password, user.password) :
        return user

def identify(payload) :
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)