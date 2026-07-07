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
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    /* Accent Buttons */
    .stButton>button {
        background-color: #00f2fe;
        color: #000000 !important;
        font-weight: 800;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #4facfe;
        transform: scale(1.02);
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
        title = {'text': "ATS Match Rate", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#00f2fe"},
            'bgcolor': "rgba(0,0,0,0)",
            'steps': [
                {'range': [0, 50], 'color': "rgba(255, 99, 132, 0.3)"},
                {'range': [50, 80], 'color': "rgba(255, 206, 86, 0.3)"},
                {'range': [80, 100], 'color': "rgba(75, 192, 192, 0.3)"}],
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor="rgba(0,0,0,0)")
    return fig

# -------------------------------
# UI Layout
# -------------------------------
st.title("⚡ Nexus AI Engine")
st.markdown("Upload your resume and target role to generate a data-driven application strategy.")

jd_templates = {
    "AWS Cloud Infrastructure Engineer": "Looking for a Cloud Engineer skilled in AWS Well-Architected Framework, EC2, S3, Docker, Kubernetes, CI/CD, Python, and Infrastructure as Code.",
    "Security & Cryptography Analyst": "Seeking an analyst with deep knowledge of RSA algorithms, data structures, network security protocols, Python, and penetration testing.",
    "Data Scientist / AI Engineer": "Seeking an AI engineer skilled in Machine Learning, Neural Networks, Python, TensorFlow, PyTorch, RAG architectures, and SQL."
}

col1, col2 = st.columns([1, 1.5])
with col1:
    uploaded_file = st.file_uploader("Drop Resume PDF", type=["pdf"])
with col2:
    selected_role = st.selectbox("Select Target Role", list(jd_templates.keys()) + ["Custom Job Description"])
    job_description = st.text_area("Requirements", jd_templates.get(selected_role, ""), height=120)

# -------------------------------
# Processing Engine
# -------------------------------
if uploaded_file and st.button("Initialize Scan", type="primary", use_container_width=True):
    with st.spinner("Extracting parameters and running NLP analysis..."):
        time.sleep(1) # Fake loading for dramatic effect
        st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
        st.session_state.skills = extract_skills(st.session_state.resume_text)
        st.session_state.missing = missing_skills(st.session_state.skills, job_description)
        st.session_state.ats_score = calculate_ats_score(st.session_state.skills, st.session_state.missing, st.session_state.resume_text)
        
        # Automatically generate the JSON review in the background
        st.session_state.ai_review = generate_resume_review(
            st.session_state.resume_text, job_description, st.session_state.skills, 
            st.session_state.missing, st.session_state.ats_score
        )

# -------------------------------
# Results Dashboard
# -------------------------------
if st.session_state.resume_text:
    st.divider()
    
    t1, t2, t3 = st.tabs(["📊 Analytics", "🧠 AI Deep Dive", "🤖 Career Chat"])
    
    with t1:
        c1, c2 = st.columns([1.5, 1])
        with c1:
            st.plotly_chart(draw_gauge(st.session_state.ats_score), use_container_width=True)
        with c2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.subheader("Skill Matrix")
            st.success(f"✅ Found: {len(st.session_state.skills)} keywords")
            st.error(f"⚠️ Missing: {len(st.session_state.missing)} keywords")
            with st.expander("View Missing Skills"):
                st.write(", ".join(st.session_state.missing))
            st.markdown('</div>', unsafe_allow_html=True)

    with t2:
        review_data = st.session_state.ai_review
        
        if "error" in review_data:
            st.error(f"Analysis failed: {review_data['error']}")
        else:
            st.markdown(f"### 🎯 Executive Summary\n> {review_data.get('executive_summary', '')}")
            
            col_s, col_w = st.columns(2)
            with col_s:
                st.markdown("#### 💪 Core Strengths")
                for s in review_data.get('strengths', []): st.write(f"✅ {s}")
            with col_w:
                st.markdown("#### 🚩 Risk Areas")
                for w in review_data.get('weaknesses', []): st.write(f"⚠️ {w}")
            
            st.divider()
            st.markdown("#### ✍️ Bullet Point Surgery (Before & After)")
            for bullet in review_data.get('bullet_point_improvements', []):
                with st.expander(f"Fix: '{bullet.get('before')}'"):
                    st.error(f"❌ {bullet.get('before')}")
                    st.success(f"✅ {bullet.get('after')}")

    with t3:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

        if prompt := st.chat_input("Ask how to tailor your resume for this specific role..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing..."):
                    answer = chat_with_resume(prompt, st.session_state.resume_text, job_description, st.session_state.skills, st.session_state.missing)
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})

        
         