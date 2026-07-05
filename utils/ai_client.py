import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


# --------------------------------
# Helper - Create Gemini AI Client
# --------------------------------

def get_ai_client():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return None

    return genai.Client(
        api_key=api_key
    )


# --------------------------------
# AI Resume Review
# --------------------------------

def generate_resume_review(
    resume_text,
    job_description,
    skills,
    missing_skills,
    ats_score
):

    client = get_ai_client()


    # Demo Mode
    if not client:

        return f"""
🧠 AI Resume Review (Demo Mode)

## Strengths

✅ Detected Skills:
{', '.join(skills[:5])}

✅ Resume is ATS readable


## Areas To Improve

- Add missing skills:
{', '.join(missing_skills)}

- Add measurable achievements
- Mention technologies used
- Add GitHub/deployment links


## Suggestion

Use:

Action + Technology + Result


Example:

❌ Built ML model

✅ Developed ML model using Python improving accuracy.
"""


    prompt = f"""
You are an expert AI resume reviewer.

Analyze this resume:


Resume:
{resume_text[:4000]}


Target Job:
{job_description}


ATS Score:
{ats_score}


Detected Skills:
{skills}


Missing Skills:
{missing_skills}


Give:

1. Strengths
2. Weaknesses
3. Missing technologies
4. Project improvements
5. ATS optimization tips

Keep advice practical.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


    except Exception as e:

        return f"""
AI Error:

{e}
"""



# --------------------------------
# Resume Chat Assistant
# --------------------------------

def chat_with_resume(
    question,
    resume_text,
    job_description,
    skills,
    missing
):

    client = get_ai_client()


    if not client:

        return f"""
🤖 Resume Chat (Demo Mode)

Question:

{question}


Suggestions:

- Improve project descriptions
- Add measurable achievements
- Mention technologies clearly
- Learn missing skills:

{', '.join(missing)}
"""


    prompt = f"""
You are an AI Career Assistant.

Answer ONLY using resume information.


Resume:

{resume_text}


Target Job:

{job_description}


Detected Skills:

{skills}


Missing Skills:

{missing}


Question:

{question}


Give practical career advice.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


    except Exception as e:

        return f"""
AI Error:

{e}
"""



# --------------------------------
# Career Roadmap Generator
# --------------------------------

def generate_career_roadmap(
    job_description,
    skills,
    missing
):

    client = get_ai_client()


    if not client:

        return f"""
🗺 Career Roadmap (Demo Mode)


## Current Skills

{', '.join(skills[:5])}


## Skills To Learn

{', '.join(missing)}


Week 1:
- Strengthen fundamentals
- Learn missing basics


Week 2:
- Learn tools
- Complete tutorials


Week 3:
- Build GitHub projects
- Deploy applications


Week 4:
- Improve resume
- Prepare interviews


Projects:

🚀 AI Chatbot

🚀 ML Web App

🚀 Dashboard Project
"""


    prompt = f"""
You are an AI Career Mentor.

Generate a personalized 30 day roadmap.


Target Job:

{job_description}


Candidate Skills:

{skills}


Missing Skills:

{missing}


Include:

1. Current analysis
2. Week 1 plan
3. Week 2 plan
4. Week 3 projects
5. Week 4 interview preparation
6. Recommended GitHub projects
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


    except Exception as e:

        return f"""
AI Error:

{e}
"""