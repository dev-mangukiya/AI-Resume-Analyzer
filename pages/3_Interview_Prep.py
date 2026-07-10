import streamlit as st
from utils.ai_client import generate_interview_prep

st.set_page_config(page_title="Interview Prep | Nexus", page_icon="🎤", layout="wide")

from utils.style import inject_custom_css
inject_custom_css()

st.title("🎤 Technical Interview Simulator")
st.markdown("Generate brutal technical interview questions targeting your specific weak spots and missing skills.")

if not st.session_state.get('resume_text'):
    st.warning("⚠️ No resume found! Please go to the Dashboard and Initialize a Scan first.")
else:
    with st.sidebar:
        st.markdown("### Context Parameters")
        job_desc = st.text_area("Target Job Description", height=150, placeholder="Paste the job description here...")
        missing_skills_str = ", ".join(st.session_state.get('missing', []))
        st.text_area("Identified Missing Skills", value=missing_skills_str, disabled=True)
        
    if st.button("🔥 Generate Interrogation", type="primary", use_container_width=True):
        if not job_desc.strip():
            st.error("Please provide a target job description in the sidebar.")
        else:
            with st.spinner("The AI is reviewing your weak spots..."):
                prep_material = generate_interview_prep(
                    st.session_state.resume_text, 
                    job_desc, 
                    missing_skills_str
                )
                
                with st.container(border=True):
                    st.markdown(prep_material)
