from flask import Flask
from flask_restful import Api
from security import authenticate, identify
from flask_jwt import JWT
from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
api = Api(app)
app.secret_key = 'hdchoi'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
jwt = JWT(app, authenticate, identify)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

@app.before_first_request
def create_tables() :
    db.create_all()

if __name__ == '__main__' :
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)