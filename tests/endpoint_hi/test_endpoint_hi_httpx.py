# Проверка /hi с помощью httpx

import httpx

r = httpx.get("http://localhost:8000/hi")

print("Status code:", r.status_code)
print("Headers:", r.headers)
print("Response text:", r.text)