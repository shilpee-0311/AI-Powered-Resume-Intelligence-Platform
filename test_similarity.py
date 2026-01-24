from similarity import get_match_score

# Example texts
resume = """
Python, SQL, data analysis, pandas, numpy, statistics
"""
job_desc = """
Looking for Data Analyst with Python, SQL, Power BI, Statistics
"""

# Calculate match
score = get_match_score(resume, job_desc)
print(f"Match Score: {score}%")
