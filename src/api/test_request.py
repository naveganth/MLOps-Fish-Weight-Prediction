# Teste de requisição para a API

import requests

url = "http://localhost:8000/predict"

payload = [{
    "Species": "Bream",
    "Length1": 25.4,
    "Length2": 26.3,
    "Length3": 30.0,
    "Height": 11.52,
    "Width": 4.02
}]

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Sucesso! Peso previsto:", response.json()["predictions"][0], "g")
    else:
        print("❌ Erro:", response.text)
except Exception as e:
    print("❌ Falha na conexão. A API está ligada?", e)