import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# 📌 Step 1: Load dataset
# Example dataset should have columns like:
# length, has_https, has_at, has_dash, num_dots, label
# where label = 0 (Safe), 1 (Phishing)

data = pd.read_csv("phishing_dataset.csv")

# 📌 Step 2: Split features and labels
X = data.drop("label", axis=1)   # Features
y = data["label"]                # Target

# 📌 Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 📌 Step 4: Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 📌 Step 5: Evaluate
print("Training Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))

# 📌 Step 6: Save model
joblib.dump(model, "phishing_model.pkl")
print("✅ Model saved as phishing_model.pkl")