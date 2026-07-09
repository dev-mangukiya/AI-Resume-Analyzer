# ⚡ Nexus | AI Resume Intelligence Engine

### *A production-grade, AI-powered ATS scanner and career strategy platform.*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-orange.svg)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

Nexus is an advanced, multi-page resume analysis platform that bridges the gap between candidates and Applicant Tracking Systems (ATS). By leveraging precise NLP parsing and **Google Gemini 2.5 Flash**, the engine scores resumes against target job descriptions, generates highly tailored cover letters, and creates brutal technical interview simulations based on your weak spots.

## 🚀 Live Demo

🔗 **Try the application here:** [Nexus AI Resume Analyzer](https://dev-ai-resume-analyzer.streamlit.app/)

---

## ✨ Advanced Features

* **Multi-Page Web Architecture:** A sleek, dark-mode platform with dedicated pages for Dashboard Analytics, Cover Letters, and Interview Prep.
* **Structural ATS Simulation:** Extracts your PDF into a strict JSON schema using Gemini to show you exactly how enterprise ATS platforms (like Workday) parse your data.
* **Interactive Analytics Dashboard:** Real-time ATS compatibility scoring utilizing `Plotly` gauge charts and responsive glassmorphism UI.
* **Automated Cover Letter Generator:** Instantly drafts a highly tailored, 3-4 paragraph professional cover letter that naturally bridges your skill gaps without using annoying placeholder brackets.
* **Technical Interview Simulator:** Automatically generates targeted, challenging technical interview questions based specifically on your missing skills, complete with ideal answer strategies.
* **Zero-False-Positive NLP Engine:** Custom-built skill extraction using Regex word-boundary matrices and dynamic alias matching.
* **Persistent Conversational AI:** A native, state-managed chat interface to ask granular questions about your resume strategy.

---

## 🛠️ Technology Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python |
| **Frontend UI** | Streamlit, Plotly Graph Objects |
| **AI / LLM** | Google GenAI SDK (Gemini 2.5 Flash) |
| **Document Processing** | pdfplumber, PyPDF2 |
| **Text Analytics** | Native Regex, Custom NLP Matrix |

---

## ⚙️ Architecture & Data Flow

1. **Ingestion:** User uploads a PDF; engine attempts extraction, rewinding the byte-stream to a fallback parser if necessary.
2. **Structural AI Parsing:** Gemini 2.5 Flash strictly converts the unstructured text into a validated JSON ATS schema.
3. **Cross-Referencing:** The NLP engine scans the profile against a massive global skill database, factoring in syntax aliases and synonyms.
4. **LLM Evaluation & Content Generation:** Strictly prompted Gemini agents evaluate the parsed data, generate cover letters, and build custom interview simulations.
5. **Visualization:** `st.session_state` preserves all data globally while Streamlit renders the multi-page interactive UI.

---

## 💻 Local Installation

**1. Clone the repository:**
```bash
git clone https://github.com/dev-mangukiya/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

**2. Create a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables:**
Create a `.streamlit` folder and a `secrets.toml` file to securely store your API key.
```bash
mkdir -p .streamlit
echo 'GOOGLE_API_KEY = "your_actual_api_key_here"' > .streamlit/secrets.toml
```

**5. Initialize the Engine:**
```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
├── app.py                  # Sleek landing page & entry point
├── requirements.txt        # Optimized deployment dependencies
├── README.md               
├── .streamlit/             
│   └── secrets.toml        # Local API Key storage (Git-ignored)
├── pages/
│   ├── 1_Dashboard.py      # Core ATS scanner & analytics logic
│   ├── 2_Cover_Letter.py   # AI Cover Letter Generator UI
│   └── 3_Interview_Prep.py # Technical Interview Simulator UI
├── utils/
│   ├── ai_client.py        # Gemini JSON prompting, parsing, and chat logic
│   ├── pdf_parser.py       # Fault-tolerant document extraction
│   ├── nlp_utils.py        # Regex word boundaries and Alias Matrix
│   └── scorer.py           # ATS algorithmic scoring calculation
└── data/
    └── skills_db.py        # Master dictionary of tech stack keywords
```

---

## 🔮 Future Roadmap

* [ ] **Database Integration:** Implement Supabase/Firebase for user authentication and historical resume tracking.
* [ ] **Exportable Reports:** Generate downloadable PDF reports of the AI's critique.
* [ ] **Semantic Matching:** Move beyond keyword regex to use sentence-transformers for true semantic experience matching.

---

## 👨‍💻 Developer

**Dev Mangukiya** *AI & Data Science Student | Passionate about Machine Learning and Software Architecture*

* **LinkedIn:** [devmangukiya](https://www.linkedin.com/in/devmangukiya)
* **GitHub:** [dev-mangukiya](https://github.com/dev-mangukiya)

---

*⭐ If you found this architecture helpful, consider giving the repository a star!*
