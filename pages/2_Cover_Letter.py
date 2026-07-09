import streamlit as st
from utils.ai_client import generate_cover_letter

st.set_page_config(page_title="Cover Letter | Nexus", page_icon="✉️", layout="wide")

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

st.title("✉️ AI Cover Letter Generator")
st.markdown("Automatically draft a highly tailored cover letter based on your parsed resume and target job.")

if not st.session_state.get('resume_text'):
    st.warning("⚠️ No resume found! Please go to the Dashboard and Initialize a Scan first.")
else:
    with st.sidebar:
        st.markdown("### Job Description Context")
        # In a real app we'd share this from the dashboard, but for now we let them refine it.
        # However, to keep it simple, we use a text area.
        job_desc = st.text_area("Target Job Description", height=200, placeholder="Paste the job description here...")
        
    if st.button("✨ Generate Cover Letter", type="primary", use_container_width=True):
        if not job_desc.strip():
            st.error("Please provide a target job description in the sidebar.")
        else:
            with st.spinner("Drafting your cover letter..."):
                cover_letter = generate_cover_letter(st.session_state.resume_text, job_desc)
                
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(cover_letter)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.download_button(
                    label="Download as Text",
                    data=cover_letter,
                    file_name="Cover_Letter.txt",
                    mime="text/plain",
                    use_container_width=True
                )
