# 🛡️ JobShield AI

## AI-Powered Resume Analyzer & Fake Job Detection System

JobShield AI is a machine-learning-powered web application that combines **resume-job matching** with **fake job detection** to help job seekers evaluate their resumes and identify potentially fraudulent job postings.

The system uses **Natural Language Processing (NLP), Machine Learning, TF-IDF, Logistic Regression, Sentence Transformers, and semantic similarity** techniques.

---

## 📌 Project Overview

JobShield AI provides two main capabilities:

### 1. Resume Analysis & Job Matching

The system analyzes a candidate's resume against a target job description and provides:

- Resume-job compatibility score
- Technical skill matching
- Missing skill identification
- Keyword matching
- Semantic similarity analysis
- Recommended job roles
- Resume feedback
- Downloadable PDF report

### 2. Fake Job Detection

The system analyzes job posting information and predicts whether the posting appears legitimate or potentially fraudulent.

It uses:

- TF-IDF text representation
- Unigrams and bigrams
- Logistic Regression
- Class-balanced training
- Fraud probability prediction
- Risk classification
- Rule-based warning detection

---

## 🚀 Key Features

### 📄 Resume Analyzer

- Upload PDF or DOCX resumes
- Extract resume text
- Analyze technical skills
- Compare resume with job description
- Calculate resume-job compatibility
- Identify matched skills
- Identify missing skills
- Generate resume feedback
- Recommend relevant job roles
- Generate a downloadable PDF report

### 🛡️ Fake Job Detection

- Enter recruiter email
- Enter job title
- Enter job description
- Predict fraudulent-job probability
- Classify jobs into risk categories
- Detect suspicious patterns
- Display precautions for potentially risky postings

### 💻 Web Interface

- Flask-based backend
- HTML/CSS/JavaScript frontend
- Resume upload functionality
- Job description input
- Interactive analysis results
- Fake-job detection interface

---

## 🧠 Resume Matching Methodology

The resume matching system combines three different scoring approaches.

### 1. Semantic Similarity — 35%

The system uses the **Sentence Transformers `all-MiniLM-L6-v2` model** to convert the resume and job description into vector representations.

Cosine similarity is then used to measure their semantic similarity.

### 2. Skill Matching — 40%

The system maintains a technical skill database and extracts skills from both the resume and job description.

The skill score is calculated based on the percentage of job-required skills found in the resume.

### 3. Keyword Matching — 25%

The system compares important words appearing in the resume and job description after basic text cleaning and stop-word filtering.

### Final Compatibility Score

```text
Final Score =
    35% Semantic Similarity
  + 40% Skill Matching
  + 25% Keyword Matching
  🤖 Fake Job Detection Methodology

The fake-job detection module uses a supervised machine learning pipeline.

Step 1 — Dataset

The model is trained using labeled job-posting data containing legitimate and fraudulent postings.

Step 2 — Text Preparation

The training data combines:

Job title
Job description
Location
Company profile
Requirements

The text is normalized and cleaned before training.

Step 3 — TF-IDF Vectorization

The text is converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency).

The model uses:

Maximum 8,000 features
Unigrams and bigrams
English stop-word removal
Step 4 — Logistic Regression

A Logistic Regression classifier is trained with:

max_iter = 2000
class_weight = balanced

Using class_weight="balanced" helps handle class imbalance between legitimate and fraudulent job postings.

Step 5 — Prediction

For a new job posting, the trained pipeline produces a fraud probability.

The application classifies the result into risk categories:

80% or higher  → Scam
45%–79.99%     → Medium Risk
Below 45%      → Legit

🔍 System Workflow
                         JobShield AI
                              |
             +----------------+----------------+
             |                                 |
             ▼                                 ▼
      Resume Analyzer                    Fake Job Detector
             |                                 |
      Upload Resume                    Email + Title +
             |                         Job Description
             ▼                                 |
      Text Extraction                         ▼
             |                         Text Processing
             ▼                                 |
      Skill Extraction                        ▼
             |                          TF-IDF Features
             ▼                                 |
      +------+------+                          ▼
      |      |     |                    Logistic Regression
      ▼      ▼     ▼                          |
   Skills Keywords Semantic                   ▼
   Score   Score   Score                Fraud Probability
      |      |       |                        |
      +------+-------+                        ▼
             |                           Risk Category
             ▼
      Final Match Score
             |
             ▼
     Skill Gap Analysis
             |
             ▼
      Resume Feedback
             |
             ▼
        PDF Report


🛠️ Technologies Used


Programming Language
Python

Machine Learning & NLP
Scikit-learn
TF-IDF
Logistic Regression
Sentence Transformers
all-MiniLM-L6-v2
Cosine Similarity
NLTK
NumPy
Pandas
Resume Processing
PDFPlumber
python-docx

Backend
Flask
Gunicorn

Frontend
HTML
CSS
JavaScript
Bootstrap

Development Tools
VS Code
Git
GitHub

📂 Project Structure
JobShieldAI/
│
├── data/
│   ├── fake_job_postings.csv
│   ├── training/
│   └── ...
│
├── dataset/
│   └── jobs.csv
│
├── scripts/
│   ├── create_doc2vec_data.py
│   ├── create_glove_corpus.py
│   ├── create_sbert_data.py
│   └── ...
│
├── static/
│   ├── logo.png
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── scam_checker.html
│   ├── scam_result.html
│   └── upload_jd.html
│
├── app.py
├── config.py
├── data_loader.py
├── feedback_engine.py
├── matching_engine.py
├── resume_parser.py
├── resume_processor.py
├── scam_model.py
├── skill_analyzer.py
├── skill_extractor.py
├── train_model.py
├── warning_engine.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── SECURITY.md
└── README.md


📊 Model Evaluation

The fake-job detection model can be evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

For fraud detection, accuracy alone is not sufficient. Precision, recall, and F1-score provide a better understanding of how effectively the model identifies fraudulent postings.

🔐 Security Considerations

The application should consider:

File type validation
File size restrictions
User input validation
Sanitization of uploaded content
Secure handling of resume files
Avoiding unnecessary storage of personal information
Secure management of application secrets

🔮 Future Enhancements
Possible improvements include:

ATS-style resume scoring
Advanced Named Entity Recognition for skill extraction
Improved semantic similarity models
Support for additional resume formats
Explainable AI for fake-job predictions
Personalized job recommendations
Resume improvement suggestions
Job portal integration
Cloud deployment
Authentication and user profiles
Analytics dashboard
Additional fraud-detection features using job-posting metadata

🎯 Use Cases
Job Seekers
Analyze resume-job compatibility
Identify missing skills
Improve resume relevance
Detect potentially suspicious job postings

Recruiters
Perform initial resume screening
Compare candidate skills with job requirements
Identify relevant candidates more efficiently

Students
Learn practical NLP and Machine Learning
Understand semantic similarity
Build an end-to-end ML web application
Gain experience with Flask and deployment

⭐ Project Highlights
Combines Machine Learning, NLP, and Web Development
Uses TF-IDF and Logistic Regression for fake-job classification
Uses Sentence Transformers and cosine similarity for semantic resume-job matching
Uses explicit skill matching and keyword analysis
Supports PDF and DOCX resume processing
Provides skill-gap analysis and feedback
Generates downloadable PDF reports
Demonstrates an end-to-end machine learning workflow
Provides a practical solution for job seekers and recruiters

💡 Skills Demonstrated
Python
Machine Learning
Natural Language Processing
Text Classification
TF-IDF
Logistic Regression
Sentence Transformers
Semantic Similarity
Cosine Similarity
Scikit-learn
NLTK
Pandas
NumPy
Flask
HTML
CSS
JavaScript
Bootstrap
Git
GitHub
Model Deployment

👩‍💻 Author

Shravani Jadhav
B.Tech Computer Science & Engineering