import requests
import json

data = [{
    "user_id": 1,
    "name": "xpg core reactor",
    "target_price": 600
}]

response = requests.post("http://localhost:5100/products", json=data)

data = [{
    "products": response.json()["products"],
    "stores": ["kabum", "terabyte", "mercado-livre"]
}]

response = requests.get("http://localhost:5060/", json=data)

print(response.json(), response.status_code)