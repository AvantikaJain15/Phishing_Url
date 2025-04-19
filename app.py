import streamlit as st
import pandas as pd
import numpy as np
import joblib
import re

# Load the trained model
model = joblib.load("final_model.pkl")  # Make sure you have this model saved

# Load the encoder if needed (optional)
# encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="🔐 Phishing URL Detector", layout="centered")
st.title("🔐 Phishing URL Detector")
st.markdown("Check if a URL is **legitimate** or **phishing**.")

st.markdown("---")

# Input form
url_input = st.text_input("🔗 Enter URL to check:")

# Optionally: Upload CSV with URLs
uploaded_file = st.file_uploader("📁 Or upload a CSV file of URLs", type=["csv"])

def extract_features(url):
    return {
        'URLLength': len(url),
        'HasHTTPS': int("https" in url.lower()),
        'NoOfSubDomain': url.count('.') - 1,
        'NoOfQMarkInURL': url.count('?'),
        'NoOfEqualsInURL': url.count('='),
        'NoOfAmpersandInURL': url.count('&'),
        'SpacialCharRatioInURL': len(re.findall(r'[^A-Za-z0-9]', url)) / len(url),
    }

def predict_url(url):
    features = extract_features(url)
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return "🚨 Phishing" if prediction == 1 else "✅ Legitimate"

# Predict for single input
if url_input:
    st.markdown("### 🧠 Prediction Result:")
    result = predict_url(url_input)
    st.success(f"Result for entered URL: **{result}**")

# Predict from uploaded file
if uploaded_file is not None:
    try:
        df_urls = pd.read_csv(uploaded_file)
        if 'URL' not in df_urls.columns:
            st.error("CSV must contain a column named 'URL'")
        else:
            df_urls['Result'] = df_urls['URL'].apply(predict_url)
            st.markdown("### 🧠 Predictions for Uploaded File:")
            st.dataframe(df_urls[['URL', 'Result']])
    except Exception as e:
        st.error(f"Error processing file: {e}")
