import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'type': '2 ltr Bottle', 'price': 120, 'qty': 200},
    'coke': {'type': '500 ml Bottle', 'price':45, 'qty': 450},
    'thumbs_up': {'type': '300 ml CAN', 'price': 50, 'qty': 100}
}

class Product(Resource):

    def get(self, product):
        return {product : products[product]}

    def put(self, product):
        products[product]['cat'] = request.form['cat']
        print(products[product])
        return {product: products[product]}

    def patch(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product][list(data.keys())[0]] = data[list(data.keys())[0]]
        return {product: products[product]}

    def post(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product] = data
        return products

    def delete(self, product):
        if product in products:
            del products[product]
            return products
        else:
            return {"Keyerror" : "Invalid key, Please enter a valid key...."}

api.add_resource(Product, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)