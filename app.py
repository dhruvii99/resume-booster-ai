
import streamlit as st
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2
import docx

nltk.download('stopwords')
from nltk.corpus import stopwords

# ----------- Helper Functions -----------
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

def get_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    else:
        return uploaded_file.read().decode("utf-8")

        import PyPDF2
import docx

def get_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        return uploaded_file.read().decode("utf-8")

# ----------- Streamlit UI -----------
st.set_page_config(page_title="Resume Matcher AI", layout="centered")
st.title("🧠 Resume Matcher AI")
st.write("Match your resume against any job description instantly and boost your chances!")

# File Upload (txt or pdf)
resume_file = st.file_uploader("📄 Upload your resume (.txt or .pdf or .docx)", type=["txt", "pdf","docx"])
jd_input = st.text_area("📝 Paste the Job Description here", height=200)

if st.button("🚀 Analyze Match"):
    if resume_file is None or jd_input.strip() == "":
        st.warning("Please upload a resume and paste a job description.")
    else:
        resume_text = get_text_from_file(resume_file)
        jd_text = jd_input

        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd_text)

        jd_keywords = extract_keywords(jd_clean, top_n=20)

        matched = []
        missing = []

        for keyword in jd_keywords:
            if keyword in resume_clean:
                matched.append(keyword)
            else:
                missing.append(keyword)

        match_percent = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords.any() else 0

        # ---------- Output ----------
        st.success(f"✅ Resume Match Score: {match_percent}%")
        st.markdown(f"🟢 Matched Keywords: {', '.join(matched)}")
        st.markdown(f"🔴 Missing Keywords: {', '.join(missing)}")

        if missing:
            st.info("💡 *Tip:* Add missing keywords to your skills or project section if relevant to boost your ATS match!")

st.markdown("---")
st.caption("Made with ❤️ by Dhruvi | Resume-Booster-AI")