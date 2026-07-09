import os
import streamlit as st
import time
import plotly.graph_objects as go

from utils.pdf_parser import extract_text_from_pdf
from utils.nlp_utils import extract_skills, missing_skills
from utils.scorer import calculate_ats_score
from utils.ai_client import generate_resume_review, chat_with_resume

# -------------------------------
# Page Config & Custom Styling
# -------------------------------
st.set_page_config(page_title="Nexus | AI Resume", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    /* Global Background and Typography */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Modern Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 40px rgba(0, 242, 254, 0.15);
        border: 1px solid rgba(0, 242, 254, 0.3);
    }
    
    /* Accent Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        color: #000000 !important;
        font-weight: 800;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 20px rgba(0, 242, 254, 0.5);
    }
    
    /* Custom Metric Styling */
    div[data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 800;
        color: #00f2fe;
    }
    
    /* Header Gradient */
    .gradient-text {
        background: linear-gradient(to right, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# State Management
# -------------------------------
state_vars = ['resume_text', 'skills', 'missing', 'ats_score', 'ai_review', 'chat_history']
for var in state_vars:
    if var not in st.session_state:
        st.session_state[var] = None if var != 'chat_history' else []

# -------------------------------
# Gauge Chart Helper
# -------------------------------
def draw_gauge(score):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "ATS Match Rate", 'font': {'size': 20, 'color': '#c9d1d9'}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#4facfe"},
            'bar': {'color': "#00f2fe"},
            'bgcolor': "rgba(255,255,255,0.05)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.1)",
            'steps': [
                {'range': [0, 50], 'color': "rgba(255, 99, 132, 0.2)"},
                {'range': [50, 80], 'color': "rgba(255, 206, 86, 0.2)"},
                {'range': [80, 100], 'color': "rgba(75, 192, 192, 0.2)"}],
        }
    ))
    fig.update_layout(
        height=320, 
        margin=dict(l=20, r=20, t=50, b=20), 
        paper_bgcolor="rgba(0,0,0,0)",
        font={'color': '#c9d1d9'}
    )
    return fig

# -------------------------------
# Sidebar Layout
# -------------------------------
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'><span class='gradient-text'>⚡ Nexus Config</span></h2>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 🎯 Target Role")
    jd_templates = {
        "AWS Cloud Infrastructure Engineer": "Looking for a Cloud Engineer skilled in AWS Well-Architected Framework, EC2, S3, Docker, Kubernetes, CI/CD, Python, and Infrastructure as Code.",
        "Security & Cryptography Analyst": "Seeking an analyst with deep knowledge of RSA algorithms, data structures, network security protocols, Python, and penetration testing.",
        "Data Scientist / AI Engineer": "Seeking an AI engineer skilled in Machine Learning, Neural Networks, Python, TensorFlow, PyTorch, RAG architectures, and SQL."
    }
    selected_role = st.selectbox("Select Profile", list(jd_templates.keys()) + ["Custom Job Description"])
    job_description = st.text_area("Job Requirements", jd_templates.get(selected_role, ""), height=250)
    
    st.caption("Powered by Gemini 2.5 Flash")

# -------------------------------
# Main UI Layout
# -------------------------------
st.markdown("<h1 style='text-align: center;'><span class='gradient-text'>Nexus AI Resume Engine</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 1.1rem;'>Upload your resume to generate a data-driven application strategy.</p>", unsafe_allow_html=True)

st.write("") # Spacer

uploaded_file = st.file_uploader("Drop Resume PDF Here", type=["pdf"])

# -------------------------------
# Processing Engine
# -------------------------------
if uploaded_file and st.button("🚀 Initialize Scan", type="primary", use_container_width=True):
    # Progress Stepper
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.markdown("⏳ **Extracting document structure...**")
    st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
    progress_bar.progress(30)
    time.sleep(0.5)
    
    status_text.markdown("🧠 **Running NLP Skill extraction...**")
    st.session_state.skills = extract_skills(st.session_state.resume_text)
    st.session_state.missing = missing_skills(st.session_state.skills, job_description)
    st.session_state.ats_score = calculate_ats_score(st.session_state.skills, st.session_state.missing, st.session_state.resume_text)
    progress_bar.progress(70)
    time.sleep(0.5)
    
    status_text.markdown("🤖 **Generating AI Executive Review...**")
    st.session_state.ai_review = generate_resume_review(
        st.session_state.resume_text, job_description, st.session_state.skills, 
        st.session_state.missing, st.session_state.ats_score
    )
    progress_bar.progress(100)
    time.sleep(0.5)
    
    status_text.empty()
    progress_bar.empty()

# -------------------------------
# Results Dashboard
# -------------------------------
if st.session_state.resume_text:
    st.divider()
    
    # Overview Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ATS Match", f"{st.session_state.ats_score}%")
    m2.metric("Skills Found", len(st.session_state.skills))
    m3.metric("Missing Skills", len(st.session_state.missing))
    m4.metric("Word Count", len(st.session_state.resume_text.split()))
    
    st.write("") # Spacer
    
    t1, t2, t3 = st.tabs(["📊 Analytics", "🧠 AI Deep Dive", "💬 Career Chat"])
    
    with t1:
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.plotly_chart(draw_gauge(st.session_state.ats_score), use_container_width=True)
        with c2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("🛠️ Skill Matrix")
            st.success(f"✅ Found {len(st.session_state.skills)} keywords")
            st.error(f"⚠️ Missing {len(st.session_state.missing)} keywords")
            
            with st.expander("View Details"):
                st.markdown("**Your Skills:**")
                st.caption(", ".join(st.session_state.skills))
                st.markdown("**Target Skills Missing:**")
                st.caption(", ".join(st.session_state.missing))
            st.markdown('</div>', unsafe_allow_html=True)

    with t2:
        review_data = st.session_state.ai_review
        
        if "error" in review_data:
            st.error(f"Analysis failed: {review_data['error']}")
        else:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(f"### 🎯 Executive Summary\n> *{review_data.get('executive_summary', '')}*")
            st.markdown('</div>', unsafe_allow_html=True)
            
            col_s, col_w = st.columns(2)
            with col_s:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 💪 Core Strengths")
                for s in review_data.get('strengths', []): 
                    st.markdown(f"✅ {s}")
                st.markdown('</div>', unsafe_allow_html=True)
            with col_w:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### 🚩 Risk Areas")
                for w in review_data.get('weaknesses', []): 
                    st.markdown(f"⚠️ {w}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("#### ✍️ Bullet Point Surgery")
            for bullet in review_data.get('bullet_point_improvements', []):
                with st.expander(f"Improvement for: '{bullet.get('before')}'"):
                    st.error(f"❌ **Before:** {bullet.get('before')}")
                    st.success(f"✅ **After:** {bullet.get('after')}")

    with t3:
        st.markdown("#### 💬 Ask the AI Career Coach")
        st.caption("Ask questions about tailoring your resume, preparing for the interview, or upskilling.")
        
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]): 
                    st.markdown(msg["content"])

        if prompt := st.chat_input("E.g., How can I better highlight my AWS experience?"):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): 
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing profile..."):
                    answer = chat_with_resume(prompt, st.session_state.resume_text, job_description, st.session_state.skills, st.session_state.missing)
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})