from flask_restful import Resource, reqparse
from models.item import ItemModel
from flask_jwt import  jwt_required


class Item(Resource) :

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help = 'This field can not be blanked')
    parser.add_argument('store_id', type=int, required=True, help = 'Every item need store id')

    @jwt_required()
    def get(self, name):
       item = ItemModel.find_by_name(name)
       if item :
           return item.json()
       else :
           return {'message' : 'item not found'}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message' : f'{name} already exits'}

        data = Item.parser.parse_args()
        new_item = ItemModel(name, data['price'], data['store_id'])

        try :
            new_item.save_to_db()
        except :
            return {'message' : 'An error occurred inserting the item'}

        return new_item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item :
            item.delete_from_db()
            return {'message' : f'{name} is deleted'}
        else :
            return {'message' : f'{name} is not found'}

    def put(self, name):
        data = reqparse.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else :
            new_item = ItemModel(name, data['price'], data['store_id'])
            new_item.save_to_db()
        return item.json()


class ItemList(Resource) :
    def get(self):
        return {'items' : [item.json() for item in ItemModel.query.all()]}