import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
from playhouse.shortcuts import model_to_dict
from flask_cors import cross_origin
import json

from products import Products

app_product = Blueprint("product", __name__)

@app_product.route("/products", methods=["POST"])
@cross_origin()
def get_products():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
            
            products = Products.select().where(Products.user_id == data["user_id"])   
            product_list = []
            for product in products:
                product_list.append(model_to_dict(product).copy())       
            
            return json.dumps({"products": product_list}), 200
            
        except Exception as err:
            print(err)
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
    
@app_product.route("/products/add", methods=["POST"])
@cross_origin()
def add_product():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
              
            product = Products.create(
                name = data["name"],
                target_price = data["target_price"],
                user_id = data["user_id"]
            )     
            
            return json.dumps({"Message": "New product added successfully!!!"}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
    
@app_product.route("/products/update", methods=["POST"])
@cross_origin()
def update_product():
    if request.method == "POST":
        try:
            data = request.get_json()[0]
              
            product = Products.update(
                name = data["name"],
                target_price = data["target_price"]
            ).where(Products.id == data["id"]).execute()
            
            return json.dumps({"Message": "Product updated successfully!!!"}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only POST allowed", 405
