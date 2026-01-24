# resume_improver.py
import re

# ------------------- RESUME QUALITY -------------------
def resume_quality_score(resume_text):
    """
    Returns a score (0-10) based on sections, length, and formatting
    """
    score = 0
    resume_text = resume_text.lower()

    # Check for key sections
    sections = ["skills", "experience", "education", "projects"]
    found_sections = sum(1 for s in sections if s in resume_text)
    score += found_sections * 2  # max 8 points

    # Length check
    words = len(resume_text.split())
    if 200 <= words <= 1200:
        score += 2
    elif 1200 < words <= 2000:
        score += 1

    return round(score, 1)


# ------------------- AI IMPROVEMENT SUGGESTIONS -------------------
def improvement_suggestions(missing_skills, match_score, resume_text):
    """
    Generates actionable AI improvement tips
    """
    suggestions = []

    # 1️⃣ CORE missing skills advice
    for skill in missing_skills:
        suggestions.append(f"CORE_REQUISITE_MISSING: Integrate '{skill.upper()}' into technical section.")

    # 2️⃣ Strategic advice based on match score
    if match_score < 50:
        suggestions.append("STRATEGIC_ADVICE: Resume requires significant architectural alignment with JD.")
    elif match_score < 80:
        suggestions.append("STRATEGIC_ADVICE: Minor optimization required to reach elite candidate status.")
    else:
        suggestions.append("STRATEGIC_ADVICE: High synergy detected. Focus on project-specific metrics.")

    # 3️⃣ Resume quality based advice
    quality = resume_quality_score(resume_text)
    suggestions.append(f"RESUME_QUALITY_SCORE: {quality}/10")

    # 4️⃣ Sections missing
    sections = ["skills", "experience", "education", "projects"]
    missing_sections = [s for s in sections if s not in resume_text.lower()]
    if missing_sections:
        suggestions.append(f"Include missing sections: {', '.join(missing_sections)}")

    # 5️⃣ Quantified achievements
    pattern = re.compile(r"\d+%|\d+ years")
    if not pattern.search(resume_text.lower()):
        suggestions.append("Add quantified achievements (e.g., 'Improved model accuracy by 18%')")

    # 6️⃣ Strong action verbs
    action_verbs = ["developed", "implemented", "designed", "optimized", "led"]
    if not any(v in resume_text.lower() for v in action_verbs):
        suggestions.append("Use strong action verbs (e.g., Developed, Implemented)")

    if not suggestions:
        suggestions.append("Resume looks strong. No immediate improvements needed.")

    return suggestions, quality
