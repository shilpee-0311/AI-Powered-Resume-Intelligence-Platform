import re

# Advanced Skill Database
SKILL_DB = {
    "Technical": ["python", "machine learning", "statistics", "sql", "pandas", "numpy", "nlp", "scikit-learn", "tensorflow"],
    "Tools": ["power bi", "tableau", "excel", "git", "docker", "aws", "azure"],
    "Soft Skills": ["communication", "leadership", "problem solving", "management", "agile"]
}

def extract_experience(text):
    """Scans for experience patterns like '5+ years' or '3 years exp'."""
    patterns = [
        r'(\d+)\s*\+?\s*years',
        r'experience\s*of\s*(\d+)\s*years',
        r'(\d+)\s*year\s*exp'
    ]
    years = []
    for pattern in patterns:
        matches = re.findall(pattern, text.lower())
        years.extend([int(m) for m in matches])
    return max(years) if years else 0

def get_categorized_analysis(resume_text, job_text):
    """Categorizes found and missing skills for visualization."""
    resume_text = resume_text.lower()
    job_text = job_text.lower()
    
    analysis = {}
    for category, skills in SKILL_DB.items():
        found = [s for s in skills if s in resume_text and s in job_text]
        missing = [s for s in skills if s in job_text and s not in resume_text]
        analysis[category] = {"found": found, "missing": missing}
    return analysis

def missing_skills(resume_text, job_text):
    """Helper for simple list of missing skills."""
    analysis = get_categorized_analysis(resume_text, job_text)
    all_missing = []
    for cat in analysis:
        all_missing.extend(analysis[cat]["missing"])
    return all_missing