import requests

url = "http://localhost:8000/meu-endpoint/"  # Substitua pela URL do seu endpoint

response = requests.get(url)

if response.status_code == 200:
    print("Resposta:", response.json())
else:
    print("Erro:", response.status_code, response.text)
