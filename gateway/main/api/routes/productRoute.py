from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests

headers = {
    "Content-Type": "application/json"
}

app_product = Blueprint("product", __name__)

@app_product.route("/products", methods=["POST"])
@cross_origin()
def products():
    if request.method == "POST":
        try:
            data = request.get_json()
            response = requests.post("http://user-actions:5000/products", json.dumps(data), headers=headers)
            print(response.json())
            return json.dumps({"products": response.json()["products"]}), 200
            
        except Exception as err:
            return json.dumps({"gateway Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
