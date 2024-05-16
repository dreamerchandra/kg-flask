from flask import Flask, request
from flask_cors import CORS

from product import Product, initialize_db

app = Flask(__name__)  # creating the Flask class object


CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/products")  # decorator drfines the
def home():
    products = Product.select()
    serialized_products = []
    for product in products:
        serialized_products.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "img": product.img,
            "description": product.description
        })
    return {
        "products": serialized_products
    }

@app.route("/products", methods=["POST"])
def add_product():
    product = request.json
    id = product.get("id")
    name = product.get("name")
    price = product.get("price")
    img = product.get("img")
    description = product.get("description")
    print(product.get('id'))
    print(name, price, img, description)
    product_db = Product.create(name=name, price=price, img=img, description=description, id=id)
    return product


if __name__ == "__main__":
    initialize_db()
    app.run(debug=True, port=3000)
