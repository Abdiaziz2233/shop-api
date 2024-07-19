import os
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from extensions import bcrypt, db
from models import Item

app = Flask(__name__)
bcrypt.init_app(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Items(Resource):
    def get(self):
        items = [item.to_dict() for item in Item.query.all()]
        return make_response(jsonify(items), 200)

api.add_resource(Items, '/items')

if __name__ == '__main__':
    app.run(debug=True)
