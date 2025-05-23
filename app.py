import joblib, json, os
from pathlib import Path
from flask import Flask, request, jsonify

MODEL = joblib.load(Path(__file__).resolve().parents[1] / "model.pkl")
NUM_FEATURES = MODEL.n_features_in_  # 10 for mtcars

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "ok", 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    try:
        X = [[data[k] for k in sorted(data.keys())]]
        if len(X[0]) != NUM_FEATURES:
            raise ValueError("Wrong number of features")
        mpg = MODEL.predict(X)[0]
        return jsonify({"mpg": round(float(mpg), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
