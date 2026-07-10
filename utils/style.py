import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
        /* Base app background with animated fluid gradient */
        @keyframes fluidGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .stApp {
            background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #1e3a8a, #0f172a);
            background-size: 400% 400%;
            animation: fluidGradient 15s ease infinite;
            color: #f8fafc;
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Inter', sans-serif;
        }

        /* Glass sidebar */
        [data-testid="stSidebar"] {
            background: rgba(20, 20, 30, 0.4) !important;
            backdrop-filter: blur(24px) saturate(180%);
            -webkit-backdrop-filter: blur(24px) saturate(180%);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Sidebar collapse button */
        [data-testid="stSidebarCollapseButton"] {
            color: #fff;
        }

        /* Main app header */
        [data-testid="stHeader"] {
            background: rgba(15, 23, 42, 0.3) !important;
            backdrop-filter: blur(20px) saturate(150%);
            -webkit-backdrop-filter: blur(20px) saturate(150%);
        }

        /* Gradient text */
        .gradient-text {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        /* Glassmorphism Cards */
        .glass-card, div[data-testid="stMetric"], .stChatInputContainer {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 20px !important;
            padding: 24px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        
        .glass-card:hover {
            transform: translateY(-5px) scale(1.02);
            border-color: rgba(255, 255, 255, 0.2) !important;
            box-shadow: 0 15px 40px 0 rgba(0, 242, 254, 0.2) !important;
        }

        /* Typography tweaks for iOS feel */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        p, span, div {
            font-weight: 400;
            letter-spacing: 0.01em;
        }
        .subtitle {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.3rem;
            font-weight: 300;
        }

        /* Chat messages */
        [data-testid="stChatMessage"] {
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin-bottom: 12px;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.02)) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 99px !important; /* Pill shape */
            padding: 10px 24px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        }
        
        div.stButton > button:hover {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.05)) !important;
            border-color: rgba(255, 255, 255, 0.3) !important;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 242, 254, 0.3) !important;
        }

        div.stButton > button:active {
            transform: translateY(1px);
        }

        /* Text Inputs and Text Areas */
        div.stTextInput > div > div > input, div.stTextArea > div > div > textarea {
            background: rgba(0, 0, 0, 0.2) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border-radius: 12px !important;
            transition: all 0.3s ease !important;
        }
        
        div.stTextInput > div > div > input:focus, div.stTextArea > div > div > textarea:focus {
            border-color: rgba(0, 242, 254, 0.5) !important;
            box-shadow: 0 0 0 2px rgba(0, 242, 254, 0.2) !important;
            background: rgba(0, 0, 0, 0.3) !important;
        }

        /* Expander */
        .streamlit-expanderHeader {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(10px) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
        .streamlit-expanderContent {
            border: none !important;
            background: transparent !important;
        }
        
        /* Hide streamlit footer */
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
