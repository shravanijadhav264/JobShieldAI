from flask import Flask, render_template, request, redirect, url_for, session
import os
from resume_parser import extract_resume_text
from matching_engine import calculate_similarity, get_top_job_matches
from scam_model import predict_scam
from skill_analyzer import analyze_skill_gap
from feedback_engine import generate_feedback
from skill_extractor import extract_skills
from warning_engine import detect_warnings

app = Flask(__name__)
app.secret_key = "secret_key_change_this"

app.config["UPLOAD_FOLDER"] = "uploads"


# ---------------- HOME ----------------
@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


# ---------------- PROCESS RESUME ----------------
@app.route('/process', methods=['POST'])
def process():

    resume_text = request.form.get("resume_text", "").strip()

    uploaded_file = request.files.get("resume_file")

    final_resume = ""

    # FILE
    if uploaded_file and uploaded_file.filename != "":
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(filepath)
        final_resume = extract_resume_text(filepath)

        session["uploaded_file"] = uploaded_file.filename

    # TEXT
    elif resume_text:
        final_resume = resume_text
        session.pop("uploaded_file", None)

    else:
        return redirect(url_for("index"))

    # STORE RESUME
    session["resume"] = final_resume
    app.config["FULL_RESUME"] = final_resume

    return redirect(url_for("upload_jd"))


# ---------------- JD PAGE ----------------
@app.route('/upload_jd')
def upload_jd():
    return render_template("upload_jd.html")


# ---------------- ANALYZE ----------------
@app.route('/analyze', methods=['POST'])
def analyze():

    jd = request.form.get("jd_text", "")
    resume = session.get("resume", "")

    if not jd or not resume:
        return redirect(url_for("index"))

    match_score = calculate_similarity(resume, jd)
    jobs = get_top_job_matches(resume)
    skills = extract_skills(resume)

    # SAFE CALL (ONLY IMPORTED FUNCTION)
    skill_data = analyze_skill_gap(resume, jd)

    # SAFE fallback (prevents Jinja crash)
    if not isinstance(skill_data, dict):
        skill_data = {"matched": [], "missing": [], "match_ratio": 0}

    feedback = generate_feedback(resume, skill_data)
    session["match_score"] = match_score
    session["resume"] = resume
    session["jd"] = jd
    session["skill_data"] = skill_data
    session["feedback"] = feedback

    return render_template(
        "result.html",
        match_score=match_score,
        jobs=jobs,
        skills=skills,
        resume=resume[:300],
        jd=jd[:300],
        skill_data=skill_data,
        feedback=feedback
    )


# ---------------- RESULT PAGE ----------------
@app.route("/result")
def result():
    return render_template(
        "result.html",
        match_score=0,
        jobs=[],
        skills=[],
        skill_data={"matched": [], "missing": []},
        resume="",
        jd="", 
        feedback=[]
    )
    
# ---------------- DOWNLOAD PDF REPORT ----------------
@app.route('/download-report')
def download_report():

    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from flask import send_file

    pdf_path = "report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    # DATA
    match_score = session.get("match_score", 0)
    resume = session.get("resume", "")
    jd = session.get("jd", "")

    skill_data = session.get("skill_data", {
        "matched": [],
        "missing": []
    })

    feedback = session.get("feedback", [])

    # TITLE
    elements.append(Paragraph("JobShield AI Report", styles['Title']))
    elements.append(Spacer(1, 20))

    # SCORE
    elements.append(Paragraph(f"<b>Match Score:</b> {match_score}%", styles['BodyText']))
    elements.append(Spacer(1, 10))

    # MATCHED
    elements.append(Paragraph("<b>Matched Skills:</b>", styles['Heading2']))

    for skill in skill_data["matched"]:
        elements.append(Paragraph(f"• {skill}", styles['BodyText']))

    elements.append(Spacer(1, 10))

    # MISSING
    elements.append(Paragraph("<b>Missing Skills:</b>", styles['Heading2']))

    for skill in skill_data["missing"]:
        elements.append(Paragraph(f"• {skill}", styles['BodyText']))

    elements.append(Spacer(1, 10))

    # FEEDBACK
    elements.append(Paragraph("<b>Resume Feedback:</b>", styles['Heading2']))

    for f in feedback:
        elements.append(Paragraph(f"• {f}", styles['BodyText']))

    elements.append(Spacer(1, 10))

    # RESUME
    elements.append(Paragraph("<b>Resume Preview:</b>", styles['Heading2']))
    elements.append(Paragraph(resume[:1000], styles['BodyText']))

    elements.append(Spacer(1, 10))

    # JD
    elements.append(Paragraph("<b>Job Description Preview:</b>", styles['Heading2']))
    elements.append(Paragraph(jd[:1000], styles['BodyText']))

    # BUILD PDF
    doc.build(elements)

    return send_file(pdf_path, as_attachment=True)


# ---------------- SCAM CHECKER ----------------
@app.route('/scam-checker')
def scam_checker():
    return render_template("scam_checker.html")


@app.route('/analyze-scam', methods=['POST'])
def analyze_scam():

    email = request.form.get("email", "")
    title = request.form.get("title", "")
    description = request.form.get("description", "")

    score, label = predict_scam(email, title, description)
    warnings = detect_warnings(email, title, description)

    if label == "Scam":
        precautions = [
            "Do not pay money",
            "Do not share bank details",
            "Verify company website",
            "Check LinkedIn presence",
            "Be careful of urgency traps"
        ]
    elif label == "Medium Risk":
        precautions = [
            "Verify recruiter email",
            "Check reviews",
            "Avoid suspicious links"
        ]
    else:
        precautions = [
            "Still verify company authenticity"
        ]

    return render_template(
        "scam_result.html",
        result=label,
        score=score,
        precautions=precautions,
        warnings=warnings
    )


# ---------------- RUN ----------------
if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    print("Starting JobShield AI...")
    app.run(host="0.0.0.0", port=7860)
