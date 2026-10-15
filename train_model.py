import pandas as pd
import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def extract_features(url):
    """Convert a URL into 10 numeric features"""
    try:
        url = str(url)
        return [
            len(url),                          # length
            url.count('.'),                    # dots
            url.count('-'),                    # hyphens
            url.count('/'),                    # slashes
            url.count('_'),                    # underscores
            url.count('@'),                    # at_sign
            1 if url.startswith('https') else 0,  # https
            sum(c.isdigit() for c in url),    # digits
            url.count('.') - 1,                # subdomains
            1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0  # has_ip
        ]
    except:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("🔄 Loading phishing dataset...")

# Load the dataset
df = pd.read_csv('phishing_dataset.csv')
print(f"✅ Loaded {len(df)} URLs")
print(f"📊 Columns: {list(df.columns)}")
print(f"📊 Label values: {df['label'].unique()}")

# Convert labels to binary (0 = legitimate/safe, 1 = phishing)
df['label_binary'] = df['label'].apply(lambda x: 1 if str(x).lower() == 'phishing' else 0)

print(f"📊 Dataset breakdown:")
print(f"   Phishing URLs: {sum(df['label_binary'] == 1)}")
print(f"   Legitimate URLs: {sum(df['label_binary'] == 0)}")

# Extract features from all URLs
print("\n📊 Extracting features from URLs...")
features = []
for url in df['url']:
    features.append(extract_features(url))

X = np.array(features)
y = df['label_binary'].values

print(f"✅ Extracted {len(X)} feature vectors")
print(f"   Each vector has {len(X[0])} features")

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n📊 Training on {len(X_train)} samples")
print(f"📊 Testing on {len(X_test)} samples")

# Train Random Forest model
print("\n🧠 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n Model accuracy: {accuracy * 100:.2f}%")

# Save the model
joblib.dump(model, 'phishing_model.pkl')
print(" Model saved as 'phishing_model.pkl'")

# Test on sample URLs
print("\n Testing on sample URLs:")
test_urls = [
    'https://google.com',
    'http://paypal-secure-login.xyz',
    'https://github.com',
    'http://bankofamerica.verify-account.ru',
    'https://amazon.com',
    'https://docs.google.com'  # This was in your dataset as legitimate
]

for url in test_urls:
    features = [extract_features(url)]
    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1] * 100
    result = "🚨 PHISHING" if pred == 1 else " SAFE"
    print(f"  {url} → {result} (confidence: {prob:.1f}%)")
