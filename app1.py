from flask import Flask #request
from flask_restful import Api #reqparse
from flask_jwt import JWT #jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
#from db import db

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app1.secret_key = 'dimitris'
api = Api(app1)

#db.init_app(app1)



jwt = JWT(app1, authenticate, identity) # new endpoint /auth

#items = []    # We will store data in a database, so we no longer need the "items" list

# When we work with Flask RESTful we don't need to return jsonify items



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':

	app1.run(port = 5000, debug = True)
