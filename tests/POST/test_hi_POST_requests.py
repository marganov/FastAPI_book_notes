import requests

r = requests.post("http://localhost:8000/hi", json= {"who": "Alex"})

print("Код ответа:", r.status_code)
print("Headers:", r.headers)
print(r.json())