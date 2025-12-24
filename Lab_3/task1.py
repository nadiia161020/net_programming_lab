from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
import json
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

DATA_FILE = 'items.json'

# Користувачі для аутентифікації (Medium: можна винести в окремий файл)
users = {
    "admin": "password123"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/items', methods=['GET'])
@auth.login_required
def get_items():
    return jsonify(load_data())

@app.route('/items', methods=['POST'])
@auth.login_required
def add_item():
    data = load_data()
    new_item = request.json
    data.append(new_item)
    save_data(data)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['GET'])
@auth.login_required
def get_item(item_id):
    items = load_data()
    item = next((it for it in items if it['id'] == item_id), None)
    return jsonify(item) if item else abort(404)

@app.route('/items/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_item(item_id):
    items = load_data()
    item = next((it for it in items if it['id'] == item_id), None)
    if not item: abort(404)
    item.update(request.json)
    save_data(items)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_item(item_id):
    items = load_data()
    items = [it for it in items if it['id'] != item_id]
    save_data(items)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)