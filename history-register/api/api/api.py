from flask import Flask
from flask_cors import CORS
import json

from routes.register import app_register

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-*:3000/*"}})

app.register_blueprint(app_register)

if __name__ == "__main__":
    app.run(host="history-register", debug=True)