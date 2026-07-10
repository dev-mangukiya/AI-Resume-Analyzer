import os
import streamlit as st
import time
import plotly.graph_objects as go

from utils.pdf_parser import extract_text_from_pdf
from utils.nlp_utils import extract_skills, missing_skills
from utils.scorer import calculate_ats_score
from utils.ai_client import generate_resume_review, chat_with_resume, parse_resume_structure

# -------------------------------
# Page Config & Custom Styling
# -------------------------------
st.set_page_config(page_title="Nexus | AI Resume", page_icon="⚡", layout="wide")

from utils.style import inject_custom_css
inject_custom_css()

# -------------------------------
# State Management
# -------------------------------
state_vars = ['resume_text', 'skills', 'missing', 'ats_score', 'ai_review', 'chat_history', 'ats_structure']
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
    
    status_text.markdown("⏳ **Extracting document structure & parsing ATS fields...**")
    st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
    st.session_state.ats_structure = parse_resume_structure(st.session_state.resume_text)
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
    
    t1, t2, t3, t4 = st.tabs(["📊 Analytics", "🧠 AI Deep Dive", "💬 Career Chat", "📑 ATS Data View"])
    
    with t1:
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.plotly_chart(draw_gauge(st.session_state.ats_score), use_container_width=True)
        with c2:
            # We remove the raw HTML glass-card here because Streamlit components 
            # like st.success and st.expander cannot be wrapped this way.
            st.subheader("🛠️ Skill Matrix")
            st.success(f"✅ Found {len(st.session_state.skills)} keywords")
            st.error(f"⚠️ Missing {len(st.session_state.missing)} keywords")
            
            with st.expander("View Details"):
                st.markdown("**Your Skills:**")
                st.caption(", ".join(st.session_state.skills))
                st.markdown("**Target Skills Missing:**")
                st.caption(", ".join(st.session_state.missing))

    with t2:
        review_data = st.session_state.ai_review
        
        if "error" in review_data:
            st.error(f"Analysis failed: {review_data['error']}")
        else:
            exec_summary = review_data.get('executive_summary', '')
            st.markdown(f'<div class="glass-card"><h3>🎯 Executive Summary</h3><p><em>{exec_summary}</em></p></div>', unsafe_allow_html=True)
            
            col_s, col_w = st.columns(2)
            with col_s:
                strengths = "".join([f"<p>✅ {s}</p>" for s in review_data.get('strengths', [])])
                st.markdown(f'<div class="glass-card"><h4>💪 Core Strengths</h4>{strengths}</div>', unsafe_allow_html=True)
            with col_w:
                weaknesses = "".join([f"<p>⚠️ {w}</p>" for w in review_data.get('weaknesses', [])])
                st.markdown(f'<div class="glass-card"><h4>🚩 Risk Areas</h4>{weaknesses}</div>', unsafe_allow_html=True)
            
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

    with t4:
        st.markdown("#### 🤖 How Applicant Tracking Systems See You")
        st.caption("This is the raw, structured JSON that enterprise ATS platforms extract from your PDF.")
        if st.session_state.ats_structure:
            if "error" in st.session_state.ats_structure:
                st.error(st.session_state.ats_structure["error"])
            else:
                st.json(st.session_state.ats_structure)
        else:
            st.info("No structure parsed.")