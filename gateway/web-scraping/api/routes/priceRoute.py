import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import Blueprint, request
import requests
import json

from products import Products

app = Blueprint("product", __name__)

@app.route("/prices", methods=["GET"])
def get_products():
    if request.method == "GET":
        try:
            response = requests.get("http://smartshopper-kabum:5000/")
            return json.dumps({"Message": "YES"}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only GET allowed", 405