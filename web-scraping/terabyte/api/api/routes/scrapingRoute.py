import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
from flask_cors import cross_origin

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import json
from time import sleep
from random import randint

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')

def scraping(products, user_num):
    options.add_argument(f"user-agent={randint(1, 100)}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    prices = {}
    for product_name in products: 
        url = f"https://www.terabyteshop.com.br/busca?str={product_name}"
        driver.get(url)
        sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        product = soup.find("div", class_ = "product-item")
        new_price = product.find("div", class_="product-item__new-price").find("span")
        price = new_price.text.replace("R$", "").replace(".", "").replace(",", ".").strip()
        prices[product_name] = float(price)
    
    driver.quit()
    
    return prices

app_scraping = Blueprint("scraping", __name__)

@app_scraping.route("/", methods=["GET"])
@cross_origin()
def get_prices():
    if request.method == "GET":
        user_num = 5
        try:
            data = request.get_json()[0]
            products = data["products"]
            
            prices = scraping(products, user_num)
            
            return json.dumps({"prices": prices}), 200
            
        except Exception as err:
            return json.dumps({"Error": f"{err}"}), 501
    else:
        return "Wrong request method. Only GET allowed", 405