from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_id = max(users.keys()) + 1
    users[new_id] = data
    return jsonify({"message": "User created", "id": new_id}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    users[user_id] = request.json
    return jsonify({"message": "User updated"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)