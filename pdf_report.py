from fpdf import FPDF
import io

def generate_pdf_report_bytes(result):
    """
    Generate PDF in memory from resume analysis result.
    Returns BytesIO object that can be used with Streamlit download button.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)

    # Title
    pdf.cell(0, 10, "AI Resume Intelligence Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Candidate: {result['name']}", ln=True)
    pdf.cell(0, 10, f"Match Score: {result['score']}%", ln=True)
    pdf.cell(0, 10, f"Resume Quality: {result['quality']}/10", ln=True)
    pdf.ln(5)

    # Missing Skills
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Missing Skills:", ln=True)
    pdf.set_font("Arial", size=12)
    for skill in result["missing"]:
        pdf.cell(0, 10, f"- {skill}", ln=True)
    pdf.ln(5)

    # AI Improvement Suggestions
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "AI Improvement Suggestions:", ln=True)
    pdf.set_font("Arial", size=12)
    for tip in result["suggestions"]:
        pdf.multi_cell(0, 10, f"- {tip}")

    # ---------------- FIX ----------------
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # get PDF as bytes
    return io.BytesIO(pdf_bytes)
