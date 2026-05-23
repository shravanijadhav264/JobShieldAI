🧠 JobShield AI – Resume Matching & Fake Job Detection System

JobShield AI is an AI-powered web application that analyzes resumes, matches them with job descriptions, detects skill gaps, and identifies potential fake job postings. It uses NLP and machine learning techniques to provide intelligent career insights in real time.

🚀 Key Features
📄 Resume parsing (PDF / DOCX / text input)
🤖 AI-powered resume–job matching using Sentence Transformers
📊 Skill gap analysis (matched vs missing skills)
🧠 Fake job detection using ML classification model
⚠️ Warning indicator engine for suspicious job patterns
💼 Job role recommendations based on resume profile
📈 Match score visualization with insights
🌐 Flask-based interactive web interface

🏗️ Technology Stack
Component	Technology
Frontend	HTML5, CSS3, Bootstrap
Backend	Python, Flask
NLP Models	Sentence Transformers (SBERT)
ML Algorithms	Logistic Regression / Classification models
Text Processing	Regex, custom skill extraction
Data Handling	Pandas, NumPy
Deployment	Render / Gunicorn

📁 Project Structure
AI-Powered-Resume-Matching-and-Fake-Job-Detection-System/
│
├── app.py
├── config.py
├── matching_engine.py
├── scam_model.py
├── skill_analyzer.py
├── skill_extractor.py
├── feedback_engine.py
├── resume_parser.py
├── warning_engine.py
│
├── dataset/
│   └── jobs.csv
│
├── data/
│   ├── corpus.txt
│   ├── documents.txt
│   └── fake_job_postings.csv
│
├── scripts/
├── static/
│   ├── style.css
│   └── logo.png
│
├── templates/
│   ├── result.html
│   ├── upload_jd.html
│   ├── scam_checker.html
│   └── scam_result.html
│
├── uploads/
├── requirements.txt
└── README.md

📊 Workflow
Upload or paste resume
Enter job description
System extracts skills and analyzes match
AI computes similarity score
System detects missing skills
Fake job detector evaluates scam probability
Warning indicators (if suspicious job)
Final result displayed in UI

🧠 Core Modules
1. Resume Matching Engine
Uses Sentence Transformers (SBERT)
Computes semantic similarity between resume and job description
Outputs match score (%)
2. Skill Analyzer
Extracts skills from text using keyword matching
Finds:
Matched skills
Missing skills
Skill gap ratio
3. Fake Job Detection System
ML-based classification model
Detects scam vs legit job postings
Outputs fraud probability score
4. Warning Indicator Engine
Detects suspicious job patterns like:
urgent hiring
registration fee mentions
fake recruiter signals
Helps identify risky job posts

⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/JobShieldAI.git
cd JobShieldAI
2. Create Virtual Environment
python -m venv venv
Activate:
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
3. Install Dependencies
pip install -r requirements.txt
4. Run Application
python app.py
Open in browser:
http://127.0.0.1:5000

🌐 Deployment
This project is deployed using:
Render (recommended)
Gunicorn for production server
Start command:
gunicorn app:app

📌 Future Improvements
🏷️ Skill badges UI system
📊 Dashboard analytics for resumes
🔍 Improved scam detection accuracy
🤖 API-based real job scraping integration

👨‍💻 Author
Shravani Jadhav
📧 Contact: shravanijadhav264@gmail.com