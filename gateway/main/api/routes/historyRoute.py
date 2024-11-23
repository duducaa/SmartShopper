from flask import Blueprint, request
from flask_cors import cross_origin
import json
import requests

headers = {
    "Content-Type": "application/json"
}

app_history = Blueprint("history", __name__)

@app_history.route("/history", methods=["POST"])
@cross_origin()
def history():
    if request.method == "POST":
        try:
            data = request.get_json()
            response = requests.post("http://user-actions:5000/history", json.dumps(data), headers=headers)
            return json.dumps({"history": response.json()["history"]}), 200
            
        except Exception as err:
            return json.dumps({"gateway Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
