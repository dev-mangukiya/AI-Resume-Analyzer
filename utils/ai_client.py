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

def parse_resume_structure(resume_text):
    """
    Parses the raw resume text into a structured JSON ATS format.
    """
    client = get_ai_client()
    if not client:
        return {"error": "API Key required for structural parsing."}

    prompt = f"Parse this resume into structured data:\n\n{resume_text[:5000]}"
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""You are a strict ATS parser. Extract the resume into this exact JSON schema:
                {
                    "personal_info": {"name": "string", "email": "string", "phone": "string", "links": ["string"]},
                    "education": [{"degree": "string", "institution": "string", "year": "string"}],
                    "work_experience": [{"title": "string", "company": "string", "duration": "string", "highlights": ["string"]}],
                    "projects": [{"name": "string", "description": "string"}],
                    "certifications": ["string"]
                }
                If a field is missing, use an empty string or empty array.
                """,
                temperature=0.1,
                response_mime_type="application/json",
            )
        )
        raw_text = response.text.strip()
        if raw_text.startswith("```json"): raw_text = raw_text[7:]
        if raw_text.startswith("```"): raw_text = raw_text[3:]
        if raw_text.endswith("```"): raw_text = raw_text[:-3]
        return json.loads(raw_text.strip())
    except Exception as e:
        return {"error": str(e)}

def generate_cover_letter(resume_text, job_description):
    """
    Generates a tailored cover letter based on the resume and job description.
    """
    client = get_ai_client()
    if not client:
        return "API Key required for Cover Letter generation."

    prompt = f"Resume:\n{resume_text[:4000]}\n\nJob Description:\n{job_description}"
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""You are an expert career coach. Write a highly tailored, professional cover letter 
                based on the candidate's resume and the target job description. Do NOT use placeholder brackets like [Company Name] 
                if the data is unavailable; instead, write it so it flows naturally without needing placeholders. 
                Keep it to 3-4 impactful paragraphs.""",
                temperature=0.6,
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def generate_interview_prep(resume_text, job_description, missing_skills):
    """
    Generates targeted technical interview questions to prep for weak spots.
    """
    client = get_ai_client()
    if not client:
        return "API Key required for Interview Prep generation."

    prompt = f"Resume:\n{resume_text[:3000]}\n\nJob:\n{job_description}\n\nMissing Skills: {missing_skills}"
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""You are a senior technical interviewer. Based on the candidate's missing skills 
                and the job description, generate 5 challenging, highly specific technical interview questions 
                they are likely to be asked to compensate for their weak spots. Provide an 'Ideal Answer Strategy' for each.""",
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"