from pdf_reader import extract_text
from similarity import get_match_score
from skills import missing_skills

# --- INPUT FILES ---
resume_path = "Shilpee Srivastava.pdf"
job_desc_path = "job_description.txt"

# --- READ DATA ---
resume_text = extract_text(resume_path)

with open(job_desc_path, "r") as f:
    job_text = f.read()

# --- AI LOGIC ---
match_score = get_match_score(resume_text, job_text)
missing = missing_skills(resume_text, job_text)

# --- OUTPUT ---
print(f"\n📊 Match Score: {match_score}%")

if missing:
    print("❌ Missing Skills:", ", ".join(missing))
else:
    print("✅ No major skills missing")

# --- EXPLANATION ---
if match_score >= 80:
    print("🟢 Strong candidate")
elif match_score >= 50:
    print("🟡 Moderate match – needs improvement")
else:
    print("🔴 Low match – not suitable")
