from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests

app_price = Blueprint("price", __name__)

@app_price.route("/prices", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            response = requests.post("http://smartshopper-scraping-gateway:5000/prices", data)
            
            if response.status_code == 200:
                return json.dumps({"prices": response.json()}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405