import requests

params = {"who": "Alex"}
request = requests.get("http://localhost:8000/hi", params=params)

print(request.json())