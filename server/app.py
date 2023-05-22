from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fakeDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Items(Resource):
    def get(self):
        return fakeDatabase
    
    def post(self):
        data = request.json
        itemId = len(fakeDatabase.keys()) + 1
        fakeDatabase[itemId] = {'name':data['name']}
        return fakeDatabase
    
api.add_resource(Items, '/items')

class Item(Resource):
    def get(self, id):
        item = fakeDatabase[id]
        return item
    
    def patch(self, id):
        data = request.json
        item = fakeDatabase[id]
        item['name'] = data['name']
        return fakeDatabase

    def delete(self, id):
        del fakeDatabase[id]
        return fakeDatabase


api.add_resource(Item, '/items/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)