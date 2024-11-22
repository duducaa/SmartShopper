from flask import Flask
from flask_cors import CORS

from routes.priceRoute import app_prices

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-interface:3000/*"}})

app.register_blueprint(app_prices)

if __name__ == "__main__":
    app.run(host="smartshopper-scraping-gateway", debug=True)
