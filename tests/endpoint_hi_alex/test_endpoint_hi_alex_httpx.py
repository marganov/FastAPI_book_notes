import httpx

r = httpx.get("http://localhost:8000/hi?who=alex")

print("Response code:", r.status_code)
print("Headers:", r.headers)
print(r.content)
print(r.json())

