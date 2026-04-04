# ------------------------------------------------------------
# 🧩 LOGIC OF THE PROJECT (Rule-Based Version)
# ------------------------------------------------------------
# 1. User enters a URL in the Streamlit front-end.
#
# 2. The function check_url(url) applies rule-based checks:
#    - Rule 1: If "https" is missing → add risk score.
#    - Rule 2: If URL length > 50 characters → add risk score.
#    - Rule 3: If "@" symbol is present → add risk score.
#    - Rule 4: If "-" symbol is present → add risk score.
#
# 3. Each suspicious feature increases the score by +1.
#
# 4. Based on the score:
#    - Score = 0 → Safe ✅
#    - Score = 1–2 → Suspicious ⚠️
#    - Score ≥ 3 → Phishing ❌
#
# 5. The app displays:
#    - Result (Safe / Suspicious / Phishing)
#    - URL features (length, symbols, HTTPS usage)
#    - A bar chart visualization of feature values
#
# 6. This version is FRONT-END ONLY:
#    - No ML backend yet
#    - Purely rule-based detection
# ------------------------------------------------------------


# ------------------------------------------------------------
# 🧩 LOGIC OF THE PROJECT (Machine Learning Version)
# ------------------------------------------------------------
# 1. Collect dataset of URLs (Safe + Phishing).
#    - Features: length, has_https, has_at, has_dash, num_dots, keywords.
#    - Label: 0 = Safe, 1 = Phishing.
#
# 2. Preprocess dataset:
#    - Convert URLs into numerical features.
#    - Split into training and testing sets.
#
# 3. Train ML model (Logistic Regression):
#    - Model learns patterns from features.
#    - Finds probability that a URL is phishing.
#
# 4. Save trained model (phishing_model.pkl).
#
# 5. In Streamlit app:
#    - Extract features from user-entered URL.
#    - Pass features to trained model.
#    - Model predicts:
#        - 0 → Safe ✅
#        - 1 → Phishing ❌
#
# 6. Display results:
#    - Prediction (Safe / Phishing)
#    - Feature analysis table
#    - Graphs (accuracy, feature importance)
#
# 7. This version is BACKEND + FRONT-END:
#    - Backend ML training with scikit-learn
#    - Front-end visualization with Streamlit
# ------------------------------------------------------------