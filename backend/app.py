from flask import Flask, request
from flask_cors import CORS

from product import Product

app = Flask(__name__)  # creating the Flask class object


CORS(app, resources={r"*": {"origins": "*"}})

products = []

@app.route("/products")  # decorator drfines the
def home():
    global products
    serialized_products = []
    for product in products:
        serialized_products.append(product.__dict__)
    return {
        "products": serialized_products
    }

@app.route("/products", methods=["POST"])
def add_product():
    global products
    product = request.json
    products.append(Product(**product))
    return product


if __name__ == "__main__":
    app.run(debug=True, port=3000)
