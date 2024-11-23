import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
from flask_cors import cross_origin

from bs4 import BeautifulSoup
import requests
import json
from typing import List

# header for the request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# request

def scraping(products: List[str]):
    
    prices = {}
    for product in products:
        product_name = product["name"]
        response = requests.get(f"https://www.kabum.com.br/busca/{product_name}", headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # get the json to the products
        page_json = json.loads(soup.find(id="__NEXT_DATA__").text)
        item: dict = page_json["props"]["pageProps"]["data"]["catalogServer"]["data"][0]
        in_offer = item.get("offer")
        price = item["priceWithDiscount"] if in_offer is None else item["offer"]["priceWithDiscount"]
        prices[product_name] = price
        
        data = [{
            "product_id": product["id"],
            "store_id": 1,
            "price": price
        }]
        requests.post("http://history-register:5000/", json=data)
    
    return prices

app_scraping = Blueprint("scraping", __name__)

@app_scraping.route("/", methods=["GET"])
@cross_origin()
def get_prices():
    if request.method == "GET":
        try:
            data = request.get_json()[0]
            products = data["products"]
            
            prices = scraping(products)
            
            return json.dumps({"prices": prices}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only GET allowed", 405
