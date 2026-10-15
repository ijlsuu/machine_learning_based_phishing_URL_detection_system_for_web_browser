from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import joblib

app = Flask(__name__)
CORS(app)  # Allows your HTML to talk to Python

# Load your trained model (you'll create this once)
model = joblib.load('phishing_model.pkl')

def extract_features(url):
    """Convert URL into numbers the model understands"""
    return {
        'length': len(url),
        'dots': url.count('.'),
        'hyphens': url.count('-'),
        'slashes': url.count('/'),
        'underscores': url.count('_'),
        'at_sign': url.count('@'),
        'https': 1 if url.startswith('https') else 0,
        'digits': sum(c.isdigit() for c in url),
        'subdomains': url.count('.') - 1,
        'has_ip': 1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0
    }

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url', '')
    
    # Extract features from the URL
    features = extract_features(url)
    
    # Convert to list in correct order for model
    feature_values = [
        features['length'],
        features['dots'],
        features['hyphens'],
        features['slashes'],
        features['underscores'],
        features['at_sign'],
        features['https'],
        features['digits'],
        features['subdomains'],
        features['has_ip']
    ]
    
    # Make prediction
    prediction = model.predict([feature_values])[0]  # 0 or 1
    probability = model.predict_proba([feature_values])[0][1]  # % confidence
    
    return jsonify({
        'url': url,
        'is_phishing': bool(prediction),
        'confidence': round(float(probability) * 100, 2),
        'features': features  # Optional: show why it decided
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
