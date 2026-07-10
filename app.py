import streamlit as st

st.set_page_config(
    page_title="Nexus | AI Resume",
    page_icon="⚡",
    layout="wide",
)

from utils.style import inject_custom_css
inject_custom_css()

st.markdown("<h1 style='text-align: center;'><span class='gradient-text'>Nexus AI</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;' class='subtitle'>The Ultimate AI-Powered Career Arsenal</p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-card">
        <h1 style='font-size: 3rem;'>📊</h1>
        <h3>ATS Dashboard</h3>
        <p>Analyze your resume against any job description with surgical precision.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h1 style='font-size: 3rem;'>✉️</h1>
        <h3>Cover Letters</h3>
        <p>Instantly generate hyper-tailored cover letters that bridge your skill gaps.</p>
    </div>
    """, unsafe_allow_html=True)
    
with col3:
    st.markdown("""
    <div class="glass-card">
        <h1 style='font-size: 3rem;'>🎤</h1>
        <h3>Interview Prep</h3>
        <p>Practice with AI-generated technical questions based on your risk areas.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.markdown("<h4 style='text-align: center;'>👈 Select a tool from the sidebar to begin.</h4>", unsafe_allow_html=True)