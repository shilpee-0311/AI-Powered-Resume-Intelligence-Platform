from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(filename, data):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph(f"<b>Name:</b> {data['name']}", styles["Normal"]))
    content.append(Paragraph(f"<b>Match Score:</b> {data['score']}%", styles["Normal"]))
    content.append(Paragraph("<b>Missing Skills:</b> " + ", ".join(data["missing"]), styles["Normal"]))

    doc.build(content)
