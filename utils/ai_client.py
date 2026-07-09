import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def get_ai_client():
    """
    Safely retrieves the Google GenAI Client using either 
    Streamlit Cloud secrets or a local environment file fallback.
    """
    api_key = None
    
    # Safely check Streamlit secrets without throwing an exception if the file doesn't exist
    if hasattr(st, "secrets") and "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        
    if not api_key:
        api_key = os.getenv("GOOGLE_API_KEY")
        
    return genai.Client(api_key=api_key) if api_key else None

def generate_resume_review(resume_text, job_description, skills, missing_skills, ats_score):
    """
    Requests a structured, strict JSON evaluation from Gemini 2.5 Flash.
    """
    client = get_ai_client()

    if not client:
        return {
            "executive_summary": "Running in Demo Mode. Add your GOOGLE_API_KEY to view real AI insights.",
            "strengths": ["ATS-readable layout structural composition"],
            "weaknesses": ["Missing alignment with specific role parameters"],
            "bullet_point_improvements": [
                {"before": "Worked on projects", "after": "Architected end-to-end full-stack systems reducing processing overhead."}
            ],
            "ats_tips": ["Ensure your contact information matches standard layout frames."]
        }

    prompt = f"""
    Analyze this candidate's profile against the target job description.
    
    <resume>
    {resume_text[:4000]}
    </resume>
    
    <target_job>
    {job_description}
    </target_job>
    
    <system_metrics>
    ATS Score: {ats_score}
    Detected Skills: {skills}
    Missing Skills: {missing_skills}
    </system_metrics>
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""You are an expert technical recruiter and resume editor. You MUST return your response as a valid JSON object matching this exact schema:
                {
                    "executive_summary": "A 2-sentence direct, professional, and clear assessment",
                    "strengths": ["string", "string"],
                    "weaknesses": ["string", "string"],
                    "bullet_point_improvements": [
                        {"before": "Original weak bullet text", "after": "Action-oriented, impact-driven, and metric-supported bullet"}
                    ],
                    "ats_tips": ["string"]
                }
                """,
                temperature=0.2,
                response_mime_type="application/json",
            )
        )
        
        # Ensure we don't trip on markdown blocks just in case the LLM ignored mime_type directives
        raw_text = response.text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        return json.loads(raw_text.strip())
    except Exception as e:
        return {"error": str(e)}

def chat_with_resume(question, resume_text, job_description, skills, missing):
    """
    Handles context-aware conversation inside the chat tab.
    """
    client = get_ai_client()
    if not client: 
        return "🤖 **Demo Mode Active:** Please supply an active Google API Key to speak directly with the AI career coach."

    prompt = f"""
    Context:
    Resume Context: {resume_text[:3000]}
    Target Requirements: {job_description}
    Skills Present: {skills}
    Skills Absent: {missing}
    
    User Query: {question}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are an elite technical career mentor. Give direct, highly practical answers under 3 paragraphs.",
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        return f"Error executing request: {e}"