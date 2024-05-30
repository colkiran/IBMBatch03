
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'type': '2 ltr Bottle', 'price': 120, 'qty': 200},
    'coke': {'type': '500 ml Bottle', 'price':45, 'qty': 450},
    'thumbs_up': {'type': '300 ml CAN', 'price': 50, 'qty': 100}
}
class Products(Resource):

    def get(self, product):
        return {product : products[product]}

api.add_resource(Products, '/getproduct/<product>')

if __name__ == '__main__':
    app.run(debug=True)

