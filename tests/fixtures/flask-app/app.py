from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/api/items", methods=["GET"])
def list_items():
    return jsonify([])


@app.route("/api/items", methods=["POST"])
def create_item():
    return jsonify(request.get_json()), 201
