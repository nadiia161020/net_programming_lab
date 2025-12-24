import requests
from requests.auth import HTTPBasicAuth

URL = "http://127.0.0.1:5000/items"
AUTH = HTTPBasicAuth('admin', 'password123')

# 1. POST - Додавання товару
new_item = {"id": 2, "name": "Phone", "price": 500, "color": "black"}
response = requests.post(URL, json=new_item, auth=AUTH)
print(f"POST: {response.status_code}")

# 2. GET - Отримання всіх товарів
response = requests.get(URL, auth=AUTH)
print(f"GET ALL: {response.json()}")

# 3. PUT - Оновлення ціни
update_data = {"price": 450}
response = requests.put(f"{URL}/2", json=update_data, auth=AUTH)
print(f"PUT: {response.json()}")

# 4. DELETE - Видалення
response = requests.delete(f"{URL}/2", auth=AUTH)
print(f"DELETE: {response.status_code}")