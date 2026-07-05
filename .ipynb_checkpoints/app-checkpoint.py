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

job_description = st.text_area(
    "Paste Job Description"
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