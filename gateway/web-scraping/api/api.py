from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://smartshopper-interface:3000/*"}})

if __name__ == "__main__":
    app.run(host="smartshopper-scraping-gateway", debug=True)