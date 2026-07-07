```markdown
<div align="center">
  
# ⚡ Nexus | AI Resume Intelligence Engine

*A production-grade, AI-powered ATS scanner and career strategy platform.*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-orange.svg)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

---

Nexus is an advanced resume analysis platform that bridges the gap between candidates and Applicant Tracking Systems (ATS). By leveraging precise NLP regex parsing and **Google Gemini 2.5 Flash**, the engine scores resumes against target job descriptions and generates structured, actionable career roadmaps.

## 🚀 Live Demo

🔗 **Try the application here:** [Nexus AI Resume Analyzer](https://dev-ai-resume-analyzer.streamlit.app/)

---

## ✨ Advanced Features

* **Interactive Analytics Dashboard:** Real-time ATS compatibility scoring utilizing `Plotly` gauge charts and responsive glassmorphism UI.
* **Zero-False-Positive NLP Engine:** Custom-built skill extraction using Regex word-boundary matrices and dynamic alias matching (e.g., equates "AWS" to "Amazon Web Services").
* **Structured AI Critiques:** Forces strict `application/json` outputs from Gemini to populate dynamic "Before & After" bullet-point surgery components.
* **Persistent Conversational AI:** A native, state-managed chat interface to ask granular questions about your resume strategy.
* **Fault-Tolerant Processing:** Built-in fallback mechanisms for PDF parsing (`pdfplumber` → `PyPDF2`) and API key management (Local `.env` → Streamlit Secrets).

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
2. **Standardization:** Text is cleaned, normalized, and stripped of edge-case punctuation.
3. **Cross-Referencing:** The NLP engine scans the profile against a massive global skill database, factoring in syntax aliases and synonyms.
4. **LLM Evaluation:** A strictly prompted Gemini agent evaluates the parsed data against target job metrics, returning a validated JSON response.
5. **Visualization:** `st.session_state` preserves the data while Streamlit renders interactive tabs, charts, and expandable critique metrics.

---

## 💻 Local Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/dev-mangukiya/AI-Resume-Analyzer.git](https://github.com/dev-mangukiya/AI-Resume-Analyzer.git)
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
│── app.py                  # Main Streamlit dashboard and UI logic
│── requirements.txt        # Optimized deployment dependencies
│── README.md               
├── .streamlit/             
│   └── secrets.toml        # Local API Key storage (Git-ignored)
├── utils/
│   ├── ai_client.py        # Gemini JSON prompting and chat logic
│   ├── pdf_parser.py       # Fault-tolerant document extraction
│   ├── nlp_utils.py        # Regex word boundaries and Alias Matrix
│   └── scorer.py           # ATS algorithmic scoring calculation
├── data/
│   └── skills_db.py        # Master dictionary of tech stack keywords

```

---

## 🔮 Future Roadmap

* [ ] **Database Integration:** Implement Supabase/Firebase for user authentication and historical resume tracking.
* [ ] **Exportable Reports:** Generate downloadable PDF reports of the AI's critique.
* [ ] **Automated Interview Prep:** Dynamically generate technical screening questions based on the candidate's missing skill vectors.

---

## 👨‍💻 Developer

**Dev Mangukiya** *AI & Data Science Student | Passionate about Machine Learning and Software Architecture*

* **LinkedIn:** [devmangukiya](https://www.google.com/search?q=https://www.linkedin.com/in/devmangukiya)
* **GitHub:** [dev-mangukiya](https://github.com/dev-mangukiya)

---

*⭐ If you found this architecture helpful, consider giving the repository a star!*

```

```

