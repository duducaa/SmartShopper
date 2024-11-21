from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-interface:3000/*"}})

from routes.loginRoute import app_login

app.register_blueprint(app_login)

if __name__ == "__main__":
    app.run(host="smartshopper-gateway", debug=True)