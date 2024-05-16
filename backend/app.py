from flask import Flask
from flask_cors import CORS

app = Flask(__name__)  # creating the Flask class object


CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/products")  # decorator drfines the
def home():
    return {
        "products": [
            {
                "name": "Chicken pizza",
                "price": 100,
                "img": "https://www.foodandwine.com/thmb/Wd4lBRZz3X_8qBr69UOu2m7I2iw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-cheese-pizza-FT-RECIPE0422-31a2c938fc2546c9a07b7011658cfd05.jpg",
                "description": "This is a chicken pizza",
                "id": 1,
            },
             {
                "name": "Pasta",
                "price": 100,
                "img": "https://www.foodandwine.com/thmb/Wd4lBRZz3X_8qBr69UOu2m7I2iw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-cheese-pizza-FT-RECIPE0422-31a2c938fc2546c9a07b7011658cfd05.jpg",
                "description": "This is a chicken pizza",
                "id": 1,
            },
        ]
    }


if __name__ == "__main__":
    app.run(debug=True, port=3000)
