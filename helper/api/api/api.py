from flask import Flask
from flask_cors import CORS

from routes.loginRoute import app_login
from routes.productRoute import app_product

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper_nextjs:3000/*"}})

app.register_blueprint(app_login)
app.register_blueprint(app_product)

if __name__ == "__main__":
    app.run(host="smartshopper_flask", port=5000, debug=True)