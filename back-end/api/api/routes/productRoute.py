import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import Blueprint, request
from flask_cors import cross_origin
import json
import sqlite3
from collections import defaultdict

app_product = Blueprint("product", __name__)

@app_product.route("/product/all", methods=["GET"])
@cross_origin()
def get_products():
    if request.method == "GET":
        
        try:   
            conn = sqlite3.connect(os.getcwd() + "/data/db.sqlite3")

            c = conn.cursor()
            
            conn.execute("update prices set price = price - 50")
            conn.commit()
            
            result = c.execute("""
                select 
                    pro.product_name, 
                    pro.target_value, 
                    pro.image_path, 
                    s.store_name, 
                    pri.price, 
                    s.logo_path
                from desired_products pro                   
                inner join prices pri
                on pro.product_id = pri.product_id
                inner join stores s
                on pri.store_id = s.store_id""")
            
            data = defaultdict(lambda: {
                "name": "----",
                "target_value": -100,
                "image": "----",
                "prices": []
            })
            for r in result:
                if data[r[0]]["name"] == "----":
                    data[r[0]]["name"] = r[0]
                
                if data[r[0]]["target_value"] == -100:
                    data[r[0]]["target_value"] = r[1]
                    
                if data[r[0]]["image"] == "----":
                    data[r[0]]["image"] = r[2]
                    
                data[r[0]]["prices"].append({
                    "store": r[3],
                    "price": r[4],
                    "logo": r[5]
                })
                
                for i in data.values():
                    print(i)
                    print("\n\n\n")
            
            return json.dumps({"products": list(data.values())}), 200
                    
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only GET allowed", 405
