
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

def extract_keywords(text, top_n=20):
    tfidf = TfidfVectorizer(max_features=top_n)
    tfidf_matrix = tfidf.fit_transform([text])
    return tfidf.get_feature_names_out()

def analyze_resume_vs_jd(resume_text, jd_text):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    jd_keywords = extract_keywords(jd_clean, top_n=20)

    matched = [k for k in jd_keywords if k in resume_clean]
    missing = [k for k in jd_keywords if k not in resume_clean]
    match_percent = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords.any() else 0

    return match_percent, matched, missing