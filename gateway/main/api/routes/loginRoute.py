from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests as req

app_login = Blueprint("login", __name__)

@app_login.route("/login", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        try:
            data = request.get_json()
            print(data)
            response = req.post("http://smartshopper-login:5000/", json=data)
            result = response.json()
            
            if response.status_code == 200 and result["key"] != "":
                return json.dumps(result), 200
            else:
                return json.dumps({"Message": "Wrong credentials"}), 501
            
        except Exception as err:
            print(err)
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
