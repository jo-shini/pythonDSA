from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello from Flask</p>"


@app.post("/items")
def create_item():
    data = request.get_json(force=True)
    return jsonify(ok=True, item=data), 201
