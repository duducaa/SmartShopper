import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
from playhouse.shortcuts import model_to_dict
from flask_cors import cross_origin
import json
from collections import defaultdict

from base import db

app_history = Blueprint("history", __name__)

@app_history.route("/history", methods=["POST"])
@cross_origin()
def get_history():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            
            print("EE")
            
            
            return json.dumps({"history": history}), 200
            
        except Exception as err:
            print(err)
            return json.dumps({"user actions - Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
