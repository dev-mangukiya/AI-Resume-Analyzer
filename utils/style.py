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
        
        /* Force Dark Mode / Glassmorphism Colors */
        html, body, [class*="st-"] {
            background-color: transparent !important;
        }

        .stApp {
            background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #1e3a8a, #0f172a) !important;
            background-size: 400% 400% !important;
            animation: fluidGradient 15s ease infinite !important;
            color: #f8fafc !important;
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Inter', sans-serif !important;
        }

        /* Glass sidebar */
        [data-testid="stSidebar"] {
            background: rgba(20, 20, 30, 0.4) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Sidebar collapse button */
        [data-testid="stSidebarCollapseButton"] {
            color: #fff !important;
        }

        /* Main app header */
        [data-testid="stHeader"] {
            background: rgba(15, 23, 42, 0.3) !important;
            backdrop-filter: blur(20px) saturate(150%) !important;
            -webkit-backdrop-filter: blur(20px) saturate(150%) !important;
        }

        /* Gradient text */
        .gradient-text {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            font-weight: 800 !important;
        }

        /* Glassmorphism Cards */
        .glass-card, div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 20px !important;
            padding: 24px !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }
        
        .glass-card:hover {
            transform: translateY(-5px) scale(1.02) !important;
            border-color: rgba(255, 255, 255, 0.2) !important;
            box-shadow: 0 15px 40px 0 rgba(0, 242, 254, 0.2) !important;
        }

        /* Force ALL text to be light to combat light mode defaults */
        h1, h2, h3, h4, h5, h6, p, span, div, label, li, a {
            color: #f8fafc !important;
        }

        /* Typography tweaks for iOS feel */
        h1, h2, h3, h4, h5, h6 {
            font-weight: 700 !important;
            letter-spacing: -0.02em !important;
        }
        p, span, div, label, li {
            font-weight: 400 !important;
            letter-spacing: 0.01em !important;
        }
        .subtitle {
            color: rgba(255, 255, 255, 0.7) !important;
            font-size: 1.3rem !important;
            font-weight: 300 !important;
        }

        /* Chat messages */
        [data-testid="stChatMessage"] {
            background: rgba(255, 255, 255, 0.07) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border-radius: 16px !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            margin-bottom: 12px !important;
        }

        /* Chat Input Fixed */
        [data-testid="stChatInput"] {
            background: rgba(0, 0, 0, 0.4) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 20px !important;
        }
        [data-testid="stChatInput"] textarea {
            color: #fff !important;
            background: transparent !important;
        }
        [data-testid="stChatInput"] button {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%) !important;
            border-radius: 50% !important;
            border: none !important;
        }
        [data-testid="stChatInput"] svg {
            fill: #000 !important;
        }

        /* JSON View / ATS Data Fixed */
        [data-testid="stJson"], [data-testid="stJson"] * {
            background-color: transparent !important;
        }
        [data-testid="stJson"] {
            background: rgba(0, 0, 0, 0.3) !important;
            backdrop-filter: blur(12px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(12px) saturate(180%) !important;
            border-radius: 16px !important;
            padding: 20px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.02)) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 99px !important;
            padding: 10px 24px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        }
        
        div.stButton > button:hover {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.05)) !important;
            border-color: rgba(255, 255, 255, 0.3) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(0, 242, 254, 0.3) !important;
        }

        div.stButton > button:active {
            transform: translateY(1px) !important;
        }

        /* Inputs (Text, TextArea, File Uploader, Selectbox) */
        div.stTextInput > div > div > input, 
        div.stTextArea > div > div > textarea,
        div[data-baseweb="select"] > div {
            background: rgba(0, 0, 0, 0.2) !important;
            backdrop-filter: blur(10px) !important;
            -webkit-backdrop-filter: blur(10px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border-radius: 12px !important;
            transition: all 0.3s ease !important;
        }
        
        div.stTextInput > div > div > input:focus, 
        div.stTextArea > div > div > textarea:focus,
        div[data-baseweb="select"] > div:focus-within {
            border-color: rgba(0, 242, 254, 0.5) !important;
            box-shadow: 0 0 0 2px rgba(0, 242, 254, 0.2) !important;
            background: rgba(0, 0, 0, 0.3) !important;
        }
        
        /* Selectbox Dropdown menu */
        div[data-baseweb="popover"] > div {
            background: rgba(20, 20, 30, 0.9) !important;
            backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
        }

        /* File Uploader */
        [data-testid="stFileUploader"] {
            background: rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            border: 1px dashed rgba(255, 255, 255, 0.2) !important;
            border-radius: 20px !important;
            padding: 20px !important;
        }
        [data-testid="stFileUploader"] > div, [data-testid="stFileUploader"] > section {
            background: transparent !important;
        }
        /* Hide default file uploader button to make it cleaner */
        [data-testid="stFileUploader"] button {
            background: rgba(255, 255, 255, 0.1) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 99px !important;
            color: white !important;
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
        
        /* Sidebar Nav active item */
        [data-testid="stSidebarNav"] li div {
            background: transparent !important;
        }
        [data-testid="stSidebarNav"] li div:hover {
            background: rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Fix ugly white backgrounds in code blocks if any */
        pre {
            background: rgba(0, 0, 0, 0.3) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Hide streamlit footer */
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
