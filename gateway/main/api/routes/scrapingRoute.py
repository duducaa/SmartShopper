from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests

headers = {
    "Content-Type": "application/json"
}

app_price = Blueprint("price", __name__)

@app_price.route("/prices", methods=["POST"])
@cross_origin()
def scraping():
    if request.method == "POST":
        try:
            data = request.get_json()
            response = requests.get("http://smartshopper-scraping-gateway:5000/", json=data, headers=headers)
            
            return json.dumps({"prices": response.json()["prices"]}), 200
            
        except Exception as err:
            print(err)
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
