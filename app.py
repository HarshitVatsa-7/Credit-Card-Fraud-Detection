from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open("C:/Users/harsh/Downloads/credit_card_fraud_model (1).pkl", 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from form
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)

    # Make prediction
    prediction = model.predict(final_features)
    output = 'Fraudulent Transaction' if prediction[0]==1 else 'Legitimate Transaction'

    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
