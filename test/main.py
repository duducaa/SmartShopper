import requests
import json

data = [{
    "products": ["rtx 4070 ti"]
}]

response = requests.get("http://localhost:5080/", json=data)
print(response.json())