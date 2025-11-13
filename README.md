# 🎬 IMDB Movie Review Sentiment Analysis (Mini Project)

[Live demo](https://jaikethan-imdb-sentiment-analysis-app-khxfcw.streamlit.app/) • `TF-IDF + Logistic Regression` • **~89.8% accuracy**

---

## Overview
This is a small end-to-end NLP mini project that classifies IMDB movie reviews as **positive** or **negative**. It demonstrates data cleaning, TF-IDF feature extraction, training a Logistic Regression model, evaluation, and deployment as an interactive Streamlit app.

**Key points**
- Dataset: 50,000 IMDB reviews (Kaggle)  
- Model: TF-IDF (uni+bi-grams, top 10k features) + Logistic Regression  
- Deployed: Streamlit Cloud

---

## Live demo
Try the app:  
**https://jaikethan-imdb-sentiment-analysis-app-khxfcw.streamlit.app/**

---

## Quick results
- Train/Test split: **80% / 20%**  
- Accuracy (logistic regression + TF-IDF): **~0.8981 (89.81%)**

---

## Files in this repo
- `app.py` — Streamlit app (demo)  
- `SentimentAnalysis.ipynb` — notebook used for training (cleaning, features, models)  
- `IMDB Dataset.csv` — dataset (Kaggle) — optional to keep in repo  
- `tfidf_vectorizer.joblib`, `sentiment_logreg.joblib` — saved model + vectorizer  
- `requirements.txt` — runtime dependencies  
- `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.gitignore`

---

## How to run locally

1. Clone:
```bash
git clone https://github.com/Jaikethan/imdb-sentiment-analysis.git
cd imdb-sentiment-analysis
