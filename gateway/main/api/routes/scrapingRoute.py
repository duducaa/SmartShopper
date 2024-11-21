import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests as req

app_login = Blueprint("login", __name__)

@app_login.route("/scraping", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            response = req.post("http://smartshopper-scraping-gateway:5000/prices", data)
            
            if response.status_code == 200:
                return json.dumps({"Message": "YES"}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405