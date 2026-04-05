# 🏠 House Price Prediction

A sleek Streamlit app that estimates house prices using a pre-trained regression model. This repo is designed for rapid demonstration, interactive input, and clean deployment.

## ✨ Highlights

- **Interactive UI**: Enter house details and get a price estimate instantly.
- **Model-backed**: Uses a serialized `HousePriceModel.pkl` trained for house price prediction.
- **Minimal setup**: One Python app file and a model artifact.

## 🚀 What’s inside

- `app.py` — Streamlit interface and prediction logic.
- `HousePriceModel.pkl` — Pre-trained scikit-learn model.
- `.gitignore` — Keeps environment noise out of source control.

## 🧪 Features

- Bedrooms, bathrooms, living area, condition, and nearby schools drive the estimate.
- Beautiful emoji-enhanced Streamlit layout.
- Fast conversion from inputs to predicted price.

## 📦 Requirements

- Python 3.8+
- `streamlit`, `numpy`, `joblib`

## ▶️ Run locally

1. Create a virtual environment:

```powershell
python -m venv venv
```

2. Activate it:

```powershell
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install streamlit numpy joblib
```

4. Run the app:

```powershell
streamlit run app.py
```

5. Open the local link shown in your browser.

## 💡 Pro tip

For best results, keep the model features in sync with how the model was trained: `bedrooms`, `bathrooms`, `livingarea`, `condition`, `numberofschools`.

## 📚 Notes

- If you want to share this app, push it to GitHub and deploy on Streamlit Cloud or any Python app host.
- Add a `requirements.txt` later if you want environment reproducibility.

---

Built with clarity, speed, and a little bit of flair.