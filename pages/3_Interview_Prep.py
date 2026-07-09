import streamlit as st
from utils.ai_client import generate_interview_prep

st.set_page_config(page_title="Interview Prep | Nexus", page_icon="🎤", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px; padding: 30px; margin-top: 20px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        color: #000; font-weight: 800; border-radius: 12px; border: none;
    }
    </style>
""", unsafe_allow_html=True)

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
                
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(prep_material)
                st.markdown('</div>', unsafe_allow_html=True)
