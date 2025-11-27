from flask import jsonify, request

from app import app
from . import handlers as h

#------USER ENDPOINTS------

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


#------CATEGORY ENDPOINTS------

@app.route("/category")
def get_categories():
    return jsonify(h.category.get_categories(), 200)

@app.post("/category")
def create_category():
    data = request.get_json()
    if not data or "name" not in data:
        return h.error.error_response("Field \"name\" is required")

    category = h.category.create_category(data["name"])
    return jsonify(category), 201

@app.delete("/category")
def delete_category():
    data = request.get_json()
    if not data or "name" not in data:
        return h.error.error_response("Field \"name\" is required")

    result = h.category.delete_category(data["name"])

    if not result:
        return h.error.error_response("Category not found", 404)

    return jsonify({"message": "Category deleted"}, 200)
