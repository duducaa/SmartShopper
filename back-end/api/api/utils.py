import os, base64, matplotlib.pyplot as plt
from datetime import datetime, timedelta

def b64image(path):
    image = open(os.getcwd() + path, 'rb')
    return base64.b64encode(image.read()).decode("utf-8")

def gerar_intervalo_datas(data_inicio, data_fim):
    # Converte as strings para objetos datetime
    data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    data_fim = datetime.strptime(data_fim, "%Y-%m-%d")

    # Cria uma lista de datas no intervalo
    intervalo_datas = []
    data_atual = data_inicio
    while data_atual <= data_fim:
        intervalo_datas.append(data_atual.strftime("%Y-%m-%d"))
        data_atual += timedelta(days=1)  # Incrementa um dia

    return intervalo_datas

from bs4 import BeautifulSoup
import requests

product = "qg240y"
response = requests.get("https://lista.mercadolivre.com.br/" + product)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(soup.find("span", class_="andes-money-amount__fraction").text.strip())

response2 = requests.get("https://www.terabyteshop.com.br/busca?str=" + product)
html2 = response2.text

soup2 = BeautifulSoup(html2, "html.parser")
print(soup2.find("div", class_="product-item"))