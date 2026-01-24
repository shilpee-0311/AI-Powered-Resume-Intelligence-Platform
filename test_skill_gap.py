from skills import missing_skills

# Example resume text
resume_text = """
Python, SQL, Pandas, NumPy, Data Analysis
"""

# Example job description
job_text = """
We are looking for a Data Analyst with Python, SQL, Power BI,
Statistics, and strong communication skills.
"""

missing = missing_skills(resume_text, job_text)

print("Missing Skills:", missing)
