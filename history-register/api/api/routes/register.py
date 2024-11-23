import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
from flask_cors import cross_origin
from datetime import datetime
import json

from history import History

app_register = Blueprint("register", __name__)

@app_register.route("/", methods=["POST"])
@cross_origin()
def login():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            
            History.create(
                product_id = data["product_id"] ,
                store_id = data["store_id"],   
                price = data["price"],
                price_date = datetime.now())
                
            return json.dumps({"Message": "Price registered!!!"}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405