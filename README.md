# 🚀 Resume Booster AI – ATS Job Match Analyzer

An AI-powered resume analyzer that matches your resume with any job description (JD) and:

- 📊 Calculates match percentage
- 🔍 Shows matched & missing keywords
- 💡 Suggests how to boost your resume for better chances in Google, Amazon, etc.

Built with 💻 Python + NLP + Streamlit in under 2 hours 🚀

---

## 🔥 Live Demo

🧪 [Click here to try the web app](#) — *(link coming soon once deployed)*  
📌 Runs in browser, no login, instant results.

---

## 📸 Preview Screenshot

![screenshot](screenshot.png)  <!-- (Optional: add a screenshot if you like) -->

---

## 🧠 How It Works

1. Upload your resume (.txt)
2. Paste any job description
3. Click "Analyze"
4. Instantly see:
   - ✅ Match score (%)
   - 🟢 Keywords already present
   - 🔴 Keywords missing
   - 💡 Suggestions to improve resume

---

## 💻 Tech Stack

| Tool            | Purpose                          |
|----------------|----------------------------------|
| Python          | Core logic / backend             |
| NLTK            | Natural language processing      |
| Scikit-learn    | TF-IDF keyword extraction        |
| Streamlit       | Frontend UI in browser           |

---

## 🧪 Local Setup Instructions

`bash
git clone https://github.com/your-username/resume-booster-ai.git
cd resume-booster-ai
pip install -r requirements.txt
streamlit run app.py
