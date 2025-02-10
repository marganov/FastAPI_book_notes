import requests

r = requests.post("http://localhost:8000/hi/header", headers= {"who": "Alex"})

print("Ответ:", r.headers)
print(r.text)