def calculate_ats_score(resume_skills, missing_skills, resume_text):

    score = 0


    # 1. Skill matching score (50 points)

    total_skills = len(resume_skills) + len(missing_skills)

    if total_skills > 0:
        skill_score = (
            len(resume_skills) / total_skills
        ) * 50
    else:
        skill_score = 0


    score += skill_score


    # 2. Important sections check (20 points)

    sections = [
        "experience",
        "education",
        "skills",
        "projects"
    ]

    text_lower = resume_text.lower()

    section_score = 0

    for section in sections:
        if section in text_lower:
            section_score += 5


    score += section_score


    # 3. Resume length check (20 points)
    word_count = len(resume_text.split())

    if 300 <= word_count <= 1000:
        score += 20
    elif 100 < word_count < 300 or word_count > 1000:
        score += 10


    # 4. PDF extraction success (10 points)

    if len(resume_text) > 100:
        score += 10


    return round(score)