
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
from nltk.corpus import stopwords

# --------- Utils ---------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

def extract_keywords(text, top_n=15):
    tfidf = TfidfVectorizer(max_features=top_n)
    tfidf_matrix = tfidf.fit_transform([text])
    return tfidf.get_feature_names_out()

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# --------- Main ---------
resume_raw = read_file('resume.txt')
jd_raw = read_file('job_description.txt')

resume_clean = clean_text(resume_raw)
jd_clean = clean_text(jd_raw)

jd_keywords = extract_keywords(jd_clean, top_n=20)

matched = []
missing = []

for keyword in jd_keywords:
    if keyword in resume_clean:
        matched.append(keyword)
    else:
        missing.append(keyword)

match_percent = int((len(matched) / len(jd_keywords)) * 100)

# --------- Output ---------
print(f"✅ Match Score: {match_percent}%\n")
print(f"🟢 Matched Keywords: {', '.join(matched)}")
print(f"🔴 Missing Keywords: {', '.join(missing)}")

if missing:
    print("\n💡 Suggestion: Add these keywords in your skills or project section if applicable.")