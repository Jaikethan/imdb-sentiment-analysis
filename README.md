# 🎬 IMDB Movie Review Sentiment Analysis (Mini Project)

A beginner-friendly NLP project to classify IMDB movie reviews as **positive** or **negative** using **TF-IDF + Logistic Regression**.  
Simple, fast, and perfect for a mini-project to add to your resume.

---

## 📌 Overview
This project uses the IMDB dataset of 50,000 labeled movie reviews to build a text classification model.

It demonstrates:
- Text preprocessing  
- TF-IDF vectorization  
- Logistic Regression model  
- Evaluation (accuracy, precision, recall, F1-score)  
- Confusion matrix visualization  
- Predicting sentiment for custom user reviews  

---

## 📂 Dataset
- **Source:** https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews  
- **File used:** `IMDB Dataset.csv`

Columns:
- `review` — text of the review  
- `sentiment` — positive / negative  

---

## 🧹 Preprocessing Steps
- Remove HTML tags  
- Convert to lowercase  
- Remove URLs  
- Remove punctuation  
- Remove extra whitespace  
- Remove English stopwords  
- Final cleaned text stored as: `clean_review`

---

## 🧠 Model Used
**Logistic Regression**  
- Fast, interpretable, works extremely well with TF-IDF data  
- Vectorization: TF-IDF with 10,000 features  
- `ngram_range = (1, 2)` for added performance  

---

## 🧪 Training & Evaluation
- Train/Test split: **80% / 20%**
- Metrics reported:
  - Accuracy: 0.8981
  - Precision, Recall, F1-score
  - Confusion matrix (heatmap)


## 📊 Confusion Matrix
A seaborn heatmap is generated to show true vs predicted labels.

---

## 🔮 Predicting Custom Reviews
The notebook includes a helper function:

```python
predict_review("This movie was amazing!")
