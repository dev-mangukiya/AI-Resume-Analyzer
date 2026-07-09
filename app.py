import streamlit as st

st.set_page_config(
    page_title="Nexus | AI Resume",
    page_icon="⚡",
    layout="wide",
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Inter', sans-serif;
    }
    .gradient-text {
        background: linear-gradient(to right, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 4rem;
    }
    .subtitle {
        color: #8b949e;
        font-size: 1.5rem;
        margin-bottom: 3rem;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 242, 254, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

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