import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.nlp_utils import extract_skills, missing_skills
from utils.scorer import calculate_ats_score

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write(
    """
    Upload your resume and get:
    - ATS Score
    - Skills Analysis
    - Missing Keywords
    - AI Suggestions
    """
)

uploaded_file = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)

# -------------------------
# Preloaded Job Descriptions
# -------------------------

jd_templates = {

    "AI/ML Intern": """
We are looking for an AI/ML Intern skilled in Python, Machine Learning, Deep Learning,
NLP, Computer Vision, TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy,
LLMs, RAG, LangChain, FastAPI, Docker, Git and AWS.

Responsibilities include building ML models, data preprocessing,
model evaluation, AI application development and deployment.
""",

    "Data Analyst Intern": """
We are looking for a Data Analyst Intern with skills in SQL, Python,
Excel, Power BI, Tableau, Pandas, NumPy, Data Visualization and Statistics.

Responsibilities include cleaning data, creating dashboards,
analyzing trends and generating business insights.
""",

    "Software Developer Intern": """
We are looking for a Software Developer Intern with knowledge of Python,
Java, Data Structures, Algorithms, REST APIs, Git, Databases,
Object Oriented Programming and Web Development.

Responsibilities include developing applications, debugging,
API integration and writing clean scalable code.
""",

    "Marketing Intern": """
We are looking for a Marketing Intern skilled in Digital Marketing,
SEO, SEM, Social Media Marketing, Content Creation, Market Research,
Google Analytics, Email Marketing, Branding and Communication.

Responsibilities include running campaigns, analyzing marketing data,
creating content and improving customer engagement.
"""

}


selected_role = st.selectbox(
    "Choose Job Role",
    list(jd_templates.keys()) + ["Custom JD"]
)


if selected_role == "Custom JD":
    job_description = st.text_area(
        "Paste Custom Job Description"
    )
else:
    job_description = st.text_area(
        "Job Description",
        jd_templates[selected_role],
        height=250
    )


if uploaded_file:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)

    skills = extract_skills(resume_text)

    missing = missing_skills(
        skills,
        job_description
    )
    ats_score = calculate_ats_score(
    skills,
    missing,
    resume_text
)

    st.subheader("📄 Extracted Resume Content")

    with st.expander("View Resume Text"):
        st.write(resume_text[:2000])


        st.subheader("Analysis Result")

        col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{ats_score}%"
        )

    with col2:
        st.metric(
            "Skills Found",
            len(skills)
        )

    with col3:
        st.metric(
            "Missing Keywords",
            len(missing)
        )


    st.subheader("Skills Detected")
    st.write(skills)


    st.subheader("Missing Skills")
    st.write(missing)