from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests

app_product = Blueprint("product", __name__)

@app_product.route("/products", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            response = requests.post("http://user-actions:5000/products", data)
            
            return json.dumps({"products": response.json()}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405