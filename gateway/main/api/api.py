from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-interface:3000/*"}})

from routes.loginRoute import app_login
from routes.scrapingRoute import app_price
from routes.productRoute import app_product

app.register_blueprint(app_login)
app.register_blueprint(app_price)
app.register_blueprint(app_product)

if __name__ == "__main__":
    app.run(host="smartshopper-gateway", debug=True)