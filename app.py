# app.py
import streamlit as st
import joblib
import re

# --- Helper functions ---
def clean_text(text: str) -> str:
    """Simple cleaning: remove HTML, non-alphanum, lower, strip."""
    if not isinstance(text, str):
        return ""
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"http\S+|www\S+|https\S+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

@st.cache_data(show_spinner=False)
def load_models():
    """Load model and vectorizer once and cache them."""
    tfidf = joblib.load("tfidf_vectorizer.joblib")
    model = joblib.load("sentiment_logreg.joblib")
    return tfidf, model

# --- Streamlit UI ---
st.set_page_config(page_title="IMDB Sentiment (Mini Project)", layout="centered")

st.title("🎬 IMDB Movie Review Sentiment Classifier")
st.write("Paste a movie review below and get a sentiment prediction (positive / negative).")

tfidf, model = load_models()

with st.form("predict_form"):
    review = st.text_area("Enter movie review", height=180, placeholder="Type or paste a review...")
    submit = st.form_submit_button("Predict")

if submit:
    if not review.strip():
        st.warning("Please enter a review to predict.")
    else:
        cleaned = clean_text(review)
        vec = tfidf.transform([cleaned])
        pred = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0].max()
        label = "Positive" if pred == 1 else "Negative"

        # Result card
        st.markdown("### Result")
        col1, col2 = st.columns([1,3])
        with col1:
            if label == "Positive":
                st.success(label)
            else:
                st.error(label)
        with col2:
            st.write(f"Confidence: **{proba:.2%}**")
            st.write(f"Raw prediction: `{pred}`")

        # Optional: show short explanation of top features (quick)
        try:
            # show top 6 features by coef sign for that class (not per-sample SHAP)
            coefs = model.coef_[0]
            feat_names = tfidf.get_feature_names_out()
            top_pos_idx = list(coefs.argsort()[-6:][::-1])
            top_neg_idx = list(coefs.argsort()[:6])
            st.markdown("**Top positive indicator words:** " + ", ".join(feat_names[i] for i in top_pos_idx))
            st.markdown("**Top negative indicator words:** " + ", ".join(feat_names[i] for i in top_neg_idx))
        except Exception:
            # not critical if it fails
            pass

st.markdown("---")
st.markdown("Project: IMDB Sentiment Analysis — TF-IDF + Logistic Regression")
st.markdown("Model files used: `tfidf_vectorizer.joblib`, `sentiment_logreg.joblib`")
