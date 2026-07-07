import re
from data.skills_db import SKILLS

# ---------------------------------------------------------
# Advanced Skill Alias Matrix
# Maps common variations and synonyms to standard skill names
# ---------------------------------------------------------
SKILL_ALIASES = {
    "aws": ["amazon web services", "aws cloud"],
    "react": ["reactjs", "react.js", "react native"],
    "vue": ["vuejs", "vue.js"],
    "node.js": ["nodejs", "node"],
    "docker": ["containerization", "docker containers"],
    "kubernetes": ["k8s", "kube"],
    "machine learning": ["ml", "machine-learning"],
    "deep learning": ["dl", "deep-learning"],
    "natural language processing": ["nlp"],
    "artificial intelligence": ["ai"],
    "cybersecurity": ["cyber security", "infosec", "penetration testing"],
    "power bi": ["powerbi", "microsoft power bi"],
    "sql": ["mysql", "postgresql", "sqlite", "t-sql"],
    "mongodb": ["mongo", "documentdb"]
}

def normalize_text(text: str) -> str:
    """
    Cleans and standardizes input text for optimal NLP parsing.
    Removes redundant whitespace and special punctuation configurations.
    """
    if not text:
        return ""
    text = text.lower()
    # Normalize spacing around slashes and dashes (e.g., "CI / CD" -> "ci/cd")
    text = re.sub(r'\s*/\s*', '/', text)
    text = re.sub(r'\s*-\s*', '-', text)
    return " ".join(text.split())

def get_all_variants(standard_skill: str) -> list:
    """
    Retrieves all known alternative names/aliases for a given skill.
    """
    standard_lower = standard_skill.lower()
    variants = [standard_lower]
    
    # Check if this skill has registered aliases
    if standard_lower in SKILL_ALIASES:
        variants.extend(SKILL_ALIASES[standard_lower])
        
    return list(set(variants))

def extract_skills(text: str) -> list:
    """
    Advanced Skill Extraction Engine.
    Uses regex word boundaries and an explicit alias lookup matrix 
    to evaluate professional profiles with extreme precision.
    """
    normalized_text = normalize_text(text)
    found_skills = set()

    # Iterate through your global master database of skills
    for skill in SKILLS:
        # Check every alias/variant for this skill
        variants = get_all_variants(skill)
        
        for variant in variants:
            # Handle special characters natively without breaking regex engines
            escaped_variant = re.escape(variant)
            
            # \b handles clean word boundaries. 
            # We add alternative check for starting/ending punctuation variations
            pattern = r'(?:^|[\b\s,./;:])' + escaped_variant + r'(?:$|[\b\s,./;:])'
            
            if re.search(pattern, normalized_text):
                found_skills.add(skill)
                break # Move to the next unique skill once a variant matches

    return sorted(list(found_skills))

def missing_skills(resume_skills: list, job_text: str) -> list:
    """
    Compares the extracted skill profile against job standardizations.
    """
    # 1. Extract every valid skill found within the target Job Description
    required_skills = set(extract_skills(job_text))
    
    # 2. Convert candidate resume skills to a normalized lookup set
    resume_skills_set = set(resume_skills)
    
    # 3. Perform a clean difference vector calculation
    missing = required_skills - resume_skills_set
    
    return sorted(list(missing))