from flask import jsonify, request

from app import app
from . import handlers as h

@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = h.user.get_user(user_id)
    if not user:
        return h.error.error_response("User not found", 404)
    return jsonify(user), 200

@app.post("/user")
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return h.error.error_response("Field \"name\" is required")

    user = h.user.create_user(data["name"])
    return jsonify(user), 201

@app.delete("/user/<int:user_id>")
def delete_user(user_id):
    result = h.user.delete_user(user_id)

    if not result:
        return h.error.error_response("User not found", 404)

    return jsonify({"message": "User deleted"}, 200)

@app.route("/users")
def list_users():
    return jsonify(h.user.list_users(), 200)