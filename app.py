from flask import Flask, request, jsonify
import numpy as np
import joblib  # Assuming you saved your model using joblib

# Load the trained model and scaler
model = joblib.load("best_model.pkl")  # Replace with your model file path
scaler = joblib.load("scaler.pkl")    # Replace with your scaler file path

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")
    try:
        # Convert features into numpy array
        features_array = np.array([float(x) for x in features.split(",")]).reshape(1, -1)
        # Scale features
        features_scaled = scaler.transform(features_array)
        # Predict
        prediction = model.predict(features_scaled)
        label = "Rock" if prediction[0] == 0 else "Mine"
        return jsonify({"prediction": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)