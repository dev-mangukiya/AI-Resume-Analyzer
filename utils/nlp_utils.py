from data.skills_db import SKILLS


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills



def missing_skills(resume_skills, job_text):

    job_text = job_text.lower()

    required = []

    for skill in SKILLS:

        if skill in job_text:
            required.append(skill)


    missing = list(
        set(required) - set(resume_skills)
    )

    return missing