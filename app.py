#!/usr/bin/env python3

from flask import Flask, jsonify, request
from train_model import predict

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_is_up():
    return "Server is up – Mtcars Flask API running!\n\n"


@app.route("/predict_mpg", methods=["POST"])
def start():
    to_predict = request.json  # raw dict from JSON body
    print("Incoming payload:", to_predict)

    try:
        mpg = predict(to_predict)  # train_model.py
    except Exception as err:
        return jsonify({"error": str(err)}), 400

    return jsonify({"predicted_mpg": mpg})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
