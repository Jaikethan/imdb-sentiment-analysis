[![CI](https://github.com/Jaikethan/imdb-sentiment-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/Jaikethan/imdb-sentiment-analysis/actions)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-blue.svg)](https://jaikethan-imdb-sentiment-analysis-app-khxfcw.streamlit.app/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

# 🎬 IMDB Movie Review Sentiment Analysis (Mini Project)

An end-to-end NLP project that classifies IMDB movie reviews as **positive** or **negative** using  
**TF-IDF + Logistic Regression (Accuracy ~ 89.8%)**, deployed on **Streamlit Cloud**.

---

## 🚀 Live Demo  
Try the deployed app here:  
👉 **https://jaikethan-imdb-sentiment-analysis-app-khxfcw.streamlit.app/**

Paste any movie review and instantly see the result.

---

## 🧠 Overview
This project demonstrates a complete classical NLP pipeline:

- Text cleaning & preprocessing  
- TF-IDF feature extraction (uni+bi-grams, top 10k features)  
- Logistic Regression classifier  
- Model evaluation (accuracy, F1-score, confusion matrix)  
- Streamlit web app deployment  
- Automated CI workflow using GitHub Actions  

---

## 📊 Model Performance
| Metric | Value |
|--------|--------|
| **Accuracy** | **89.81%** |
| Model | Logistic Regression |
| Features | TF-IDF (10,000 features) |

---

## 📂 Files in This Repository
```
imdb-sentiment-analysis/
│── app.py                     # Streamlit app
│── IMDB Dataset.csv           # Dataset (optional to keep)
│── tfidf_vectorizer.joblib    # Saved vectorizer
│── sentiment_logreg.joblib    # Trained classifier
│── requirements.txt           # Dependencies
│── README.md
│── LICENSE
│── CONTRIBUTING.md
│── CODE_OF_CONDUCT.md
│── .gitignore
│── .github/workflows/ci.yml   # CI pipeline
└── notebooks/
    └── SentimentAnalysis.ipynb
```

---

## 🛠 Run Locally (Developer Guide)

### 1️⃣ Clone
```bash
git clone https://github.com/Jaikethan/imdb-sentiment-analysis.git
cd imdb-sentiment-analysis
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
# OR
source venv/bin/activate    # Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start App
```bash
streamlit run app.py
```

App opens at:  
👉 http://localhost:8501

---

## 🧪 How It Works (Quick Summary)

1. **Preprocessing**  
   - Remove HTML, punctuation, extra whitespace  
   - Lowercasing  
   - Remove stopwords  

2. **Feature Extraction**  
   - TF-IDF (1-2 grams, 10k max features)

3. **Model**  
   - Logistic Regression (fast, strong baseline for text data)

4. **Deployment**  
   - Streamlit Cloud  
   - GitHub Actions CI to check code quality  

---

## 🤝 Contributing

We welcome contributions!

```bash
git checkout -b feature/my-change
```

Steps:
1. Fork repo  
2. Create feature branch  
3. Make changes  
4. Commit & push  
5. Open Pull Request  

See **CONTRIBUTING.md** for details.

---

## 📄 License  
This project is licensed under the **MIT License** — free for personal and commercial use.

---

## ⭐ Support  
If you like this project, please **star the repo**!  
It really helps. 😊
