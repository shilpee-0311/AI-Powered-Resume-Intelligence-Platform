import streamlit as st
import plotly.graph_objects as go
from pdf_reader import extract_text
from similarity import get_match_score
from skills import get_categorized_analysis, missing_skills
from resume_improver import improvement_suggestions
from pdf_report import generate_pdf_report_bytes  # returns BytesIO




# ---------------- SESSION STATE ----------------
if "results" not in st.session_state:
    st.session_state.results = []

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #05070a;
    background-image:
        linear-gradient(rgba(0,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,255,255,0.03) 1px, transparent 1px);
    background-size: 30px 30px;
}
.hud-card {
    background: rgba(10,15,25,0.95);
    border-left: 4px solid #00f2ff;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 20px;
    color: white;
}
.tech-title {
    color: #00f2ff;
    text-align: center;
    letter-spacing: 4px;
}
.score-box {
    background: #000;
    border: 1px solid #7000ff;
    color: white;
    padding: 20px;
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='tech-title'>CORE-AI // RESUME SCANNER</h1>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
c1, c2 = st.columns(2)

with c1:
    st.markdown("<div class='hud-card'>UPLOAD RESUMES</div>", unsafe_allow_html=True)
    resume_files = st.file_uploader(
        "Upload multiple resumes (PDF)",
        type=["pdf"],
        accept_multiple_files=True,
        key="multi_resume"
    )

with c2:
    st.markdown("<div class='hud-card'>JOB DESCRIPTION</div>", unsafe_allow_html=True)
    job_desc = st.text_area("Paste JD here", height=160)

analyze = st.button("RUN AI DIAGNOSTIC", key="analyze_btn")

# ---------------- RADAR CHART FUNCTION ----------------
def draw_radar_chart(analysis):
    cats = list(analysis.keys())
    scores = []

    for c in cats:
        f = len(analysis[c]["found"])
        m = len(analysis[c]["missing"])
        scores.append((f / (f + m)) * 100 if f + m else 0)

    fig = go.Figure(
        data=go.Scatterpolar(
            r=scores + [scores[0]],
            theta=cats + [cats[0]],
            fill="toself"
        )
    )
    fig.update_layout(
        polar=dict(radialaxis=dict(range=[0, 100])),
        showlegend=False,
        height=300
    )
    return fig

# ---------------- ANALYSIS ----------------
if analyze:
    if not resume_files:
        st.error("Upload at least 1 resume")
    elif not job_desc:
        st.error("Paste job description")
    else:
        st.session_state.results = []
        with st.spinner("Analyzing resumes..."):
            for resume in resume_files:
                text = extract_text(resume)
                score = get_match_score(text, job_desc)
                analysis = get_categorized_analysis(text, job_desc)
                missing = missing_skills(text, job_desc)
                suggestions, quality = improvement_suggestions(missing, score, text)

                st.session_state.results.append({
                    "name": resume.name,
                    "score": score,
                    "analysis": analysis,
                    "missing": missing,
                    "quality": quality,
                    "suggestions": suggestions
                })

# ---------------- OUTPUT ----------------
if st.session_state.results:
    st.markdown("<h2 class='tech-title'>CANDIDATE RANKING</h2>", unsafe_allow_html=True)

    for i, r in enumerate(st.session_state.results, 1):
        with st.expander(f"#{i}  {r['name']}  |  MATCH {r['score']}%"):
            # Radar Chart
            st.plotly_chart(draw_radar_chart(r["analysis"]), use_container_width=True)

            # Missing Skills
            st.write("❌ Missing Skills:", ", ".join(r["missing"]))

            # AI Improvement Suggestions
            st.markdown("💡 AI Improvement Suggestions:")
            for tip in r["suggestions"]:
                st.write("•", tip)

            # Resume Quality Score
            st.write("📝 Resume Quality Score:", r["quality"], "/10")

            # Download PDF
            pdf_bytes = generate_pdf_report_bytes(r)  # returns BytesIO
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_bytes,
                file_name=f"{r['name'].replace('.pdf','')}_report.pdf",
                mime="application/pdf"
            )
