import sys, os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(root)
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data/models')))
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'data')))

from flask import request, Blueprint
from flask_cors import cross_origin

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import json
import requests

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--headless")
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("user-agent=smartshopper")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def scraping(products):
    
    prices = {}
    for product_name in products:         
        response = requests.get(f"https://lista.mercadolivre.com.br/{product_name}", headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        priceDiv = soup.find("div", class_ = "poly-card").find("div", class_ = "poly-price__current")
        with open("text.html", 'w') as file:
            file.write(soup.find("div", class_ = "poly-card").prettify())
            file.close()
        
        price_fraction = priceDiv.find("span", class_="andes-money-amount__fraction")
        price_cents = priceDiv.find("span", class_="andes-money-amount__cents") or 0
        price = price_fraction.text + ("." + price_cents.text if type(price_cents) == "str" else "")
        prices[product_name] = float(price)
    
    # driver.quit()
    
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