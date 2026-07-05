import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.nlp_utils import extract_skills, missing_skills
from utils.scorer import calculate_ats_score

from utils.ai_client import (
    generate_resume_review,
    chat_with_resume,
    generate_career_roadmap
)


# -------------------------------
# Page Config
# -------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("🚀 AI Resume Analyzer")

    st.markdown(
        """
### Your personal AI career assistant

Upload your resume, compare it with a job role,
and get AI-powered improvement suggestions.
        """
    )

    st.divider()

    st.subheader("Features")

    st.write(
        """
✅ ATS Score  
🧠 AI Resume Review  
🤖 Resume Chat  
🗺 Career Roadmap  
📊 Skill Analysis
        """
    )

    st.divider()

    st.caption(
        "Built with Python + Streamlit + Generative AI"
    )


# -------------------------------
# Main Page
# -------------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    """
Upload your resume and get:

- ATS Score
- Skills Analysis
- Missing Keywords
- AI Suggestions
- Resume Chat Assistant
    """
)


uploaded_file = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)


# -------------------------------
# Job Descriptions
# -------------------------------

jd_templates = {

    "AI/ML Intern": """
We are looking for an AI/ML Intern skilled in Python,
Machine Learning, Deep Learning, NLP, Computer Vision,
TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy,
LLMs, RAG, LangChain, FastAPI, Docker, Git and AWS.
""",

    "Data Analyst Intern": """
Looking for Data Analyst Intern skilled in SQL, Python,
Excel, Power BI, Tableau, Pandas, NumPy,
Statistics and Data Visualization.
""",

    "Software Developer Intern": """
Looking for Software Developer Intern skilled in Python,
Java, Data Structures, Algorithms, REST APIs,
Git, Databases and Web Development.
"""

}


selected_role = st.selectbox(
    "Choose Job Role",
    list(jd_templates.keys()) + ["Custom JD"]
)


if selected_role == "Custom JD":

    job_description = st.text_area(
        "Paste Job Description"
    )

else:

    job_description = st.text_area(
        "Job Description",
        jd_templates[selected_role],
        height=250
    )


# -------------------------------
# Resume Processing
# -------------------------------

if uploaded_file:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text_from_pdf(uploaded_file)


    skills = extract_skills(
        resume_text
    )


    missing = missing_skills(
        skills,
        job_description
    )


    ats_score = calculate_ats_score(
        skills,
        missing,
        resume_text
    )


    # -------------------------------
    # ATS Dashboard
    # -------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "ATS Score",
            ats_score
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



    # -------------------------------
    # AI Resume Review
    # -------------------------------

    st.divider()

    st.subheader("🧠 AI Resume Review")


    if st.button("Generate AI Feedback"):

        review = generate_resume_review(
            resume_text,
            job_description,
            skills,
            missing,
            ats_score
        )


        st.markdown(review)



    # -------------------------------
    # Resume Chat Assistant
    # -------------------------------

    st.divider()


    st.subheader("🤖 Resume Chat Assistant")


    user_question = st.text_input(
        "Ask AI about your resume"
    )


    if user_question:

        answer = chat_with_resume(
            user_question,
            resume_text,
            job_description,
            skills,
            missing
        )


        st.markdown(answer)
            # -------------------------------
    # Career Roadmap
    # -------------------------------

    st.divider()

    st.subheader("🗺 AI Career Roadmap")


    if st.button("Generate Career Roadmap"):


        roadmap = generate_career_roadmap(
            job_description,
            skills,
            missing
        )


        st.markdown(roadmap)

        
         