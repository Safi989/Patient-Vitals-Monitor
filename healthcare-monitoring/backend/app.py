from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources = {r"/api/*": {"origins": "*"}})


vitals_data = []


@app.route("/api/vitals", methods=["POST"])
def receive_vitals():
    data = request.get_json()
    vitals_data.append(data)
    print("Received: ", data)
    return jsonify({"status": "ok"}), 200


@app.route("/api/vitals", methods=["GET"])
def get_vitals():
    return jsonify(vitals_data[-100:])


if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5001, debug = True)