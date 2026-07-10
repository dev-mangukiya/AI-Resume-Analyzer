import streamlit as st
from utils.ai_client import generate_cover_letter

st.set_page_config(page_title="Cover Letter | Nexus", page_icon="✉️", layout="wide")

from utils.style import inject_custom_css
inject_custom_css()

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
                
                with st.container(border=True):
                    st.markdown(cover_letter)
                
                st.download_button(
                    label="Download as Text",
                    data=cover_letter,
                    file_name="Cover_Letter.txt",
                    mime="text/plain",
                    use_container_width=True
                )
