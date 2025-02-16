# Проверка /hi с помощью Requests

import requests

r = requests.get("http://localhost:8000/hi")

print("Status code:", r.status_code)
print("Headers:", r.headers)
print("Response text:", r.text)