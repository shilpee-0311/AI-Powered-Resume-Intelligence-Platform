from pdf_reader import extract_text
from similarity import get_match_score


resume_text = extract_text("Shilpee Srivastava.pdf")


with open("job_description.txt", "r") as f:
    job_desc = f.read()


score = get_match_score(resume_text, job_desc)

print(f"Match Score: {score}%")
