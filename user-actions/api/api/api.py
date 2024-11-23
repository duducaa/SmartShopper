from flask import Flask
from flask_cors import CORS

from routes.productRoute import app_product
from routes.priceHistoryRoute import app_history

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-gateway:5000/*"}})

app.register_blueprint(app_product)
app.register_blueprint(app_history)

if __name__ == "__main__":
    app.run(host="user-actions", debug=True)