import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import Blueprint, request
import requests
import json

app_prices = Blueprint("prices", __name__)

@app_prices.route("/", methods=["GET"])
def get_products():
    if request.method == "GET":
        try:
            data = request.get_json()[0]
            stores = data["stores"]
            products = data["products"]
            print(products)
            print(stores)
            
            prices = {product["name"]: {} for product in products}
            for store in stores:
                response = requests.get(f"http://smartshopper-{store}:5000/", json=[{
                    "products": products
                }])
                store_prices = response.json()["prices"]
                
                for k, v in store_prices.items():
                    prices[k][store] = v
                    
            return json.dumps({"prices": prices}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only GET allowed", 405
