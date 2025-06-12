# app.py
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained ensemble model
with open('ensemble_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    # Convert input JSON to DataFrame
    input_df = pd.DataFrame([data])

    # Predict
    prediction = model.predict(input_df)[0]

    # Return result
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
