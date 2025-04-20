
# 🔐 Phishing URL Detector

A machine learning-powered web application that detects whether a given URL is **legitimate** or **phishing** using handcrafted features and classification models (Random Forest & XGBoost). Built using Python and deployed with Streamlit.

---

## 📂 Project Structure

├── app.py # Streamlit app 
├── phishing-ml.ipynb # ML training and evaluation notebook 
├── best_phishing_model_*.pkl # Trained model (RandomForest or XGBoost) 
├── PhiUSIIL_Phishing_URL_Dataset.csv # Dataset used 
├── requirements.txt # Python dependencies 
└── README.md # Project description (this file)



---

## 🧠 Model Features

The model extracts meaningful features from URLs to detect phishing behavior:

- `URLLength` - Total length of the URL
- `HasHTTPS` - Whether the URL uses HTTPS
- `NoOfSubDomain` - Number of subdomains
- `NoOfQMarkInURL` - Number of `?` in the URL
- `NoOfEqualsInURL` - Number of `=` in the URL
- `NoOfAmpersandInURL` - Number of `&` in the URL
- `SpacialCharRatioInURL` - Ratio of special characters in the URL

---

## 🚀 Getting Started

### 1. Clone the repository


git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector

2. Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
Or manually:
pip install pandas numpy scikit-learn xgboost matplotlib seaborn streamlit joblib


Training the Model

If you'd like to retrain the model:
Open and run phishing-ml.ipynb
It trains both a RandomForest and XGBoost classifier
Saves the best performing model as best_phishing_model_<model>.pkl

Running the Streamlit App

streamlit run app.py
This will open a browser window with the Phishing URL Detector UI.


Output

✅ Legitimate – Safe, valid URL
🚨 Phishing – Suspicious or harmful URL detected



 License

This project is for educational and research purposes.




Acknowledgments
-PhiUSIIL Phishing Dataset
-scikit-learn, XGBoost, Streamlit, pandas, matplotlib