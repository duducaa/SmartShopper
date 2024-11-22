from flask import Flask
from flask_cors import CORS

from routes.productRoute import app_product

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-gateway:5000/*"}})

app.register_blueprint(app_product)

if __name__ == "__main__":
    app.run(host="user-actions", debug=True)