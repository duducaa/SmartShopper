import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import Blueprint, request
import json

from products import Products

app = Blueprint("product", __name__)

@app.route("/products", methods=["POST"])
def get_products():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            user_id = data["user_id"]
            
            products = Products.raw(f"select * from users_products where user_id = {user_id}")

            return json.dumps({"products": products}), 401
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405