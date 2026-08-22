# AI-Powered Resume Analyzer & Fake Job Detection System

An AI-powered web application that analyzes resumes, extracts relevant information, evaluates resume–job compatibility, and detects potentially fraudulent or fake job postings using Natural Language Processing and Machine Learning.

## Project Overview

The **AI-Powered Resume Analyzer & Fake Job Detection System** combines two useful recruitment-related capabilities into a single platform:

1. **Resume Analysis & Job Matching** – analyzes a candidate's resume against a job description and identifies relevant skills, keywords, and compatibility.
2. **Fake Job Detection** – analyzes job postings and predicts whether they are likely to be legitimate or fraudulent.

The system uses **Natural Language Processing (NLP), Machine Learning, and text similarity techniques** to automate parts of the recruitment and job-search process.

---

## Key Features

### Resume Analyzer

* Upload and analyze resumes.
* Extract important information from resume text.
* Identify technical skills and relevant keywords.
* Compare resume content with a given job description.
* Calculate resume–job compatibility.
* Highlight missing or relevant skills.
* Provide an AI-based analysis of the candidate profile.

### Fake Job Detection

* Analyze job title and job description.
* Detect suspicious or potentially fraudulent job postings.
* Use NLP-based text processing and machine learning for classification.
* Generate a prediction indicating whether a job appears legitimate or suspicious.
* Provide analysis based on textual characteristics of the job posting.

### User-Friendly Interface

* Simple web-based interface.
* Resume upload functionality.
* Job description input.
* Prediction and analysis results.
* Easy-to-understand output.

---

## Technologies Used

### Programming Language

* Python

### Machine Learning & NLP

* NLTK
* TF-IDF Vectorization
* Logistic Regression
* Sentence Transformers / Text Embeddings

### Backend / Web Framework

* Flask

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Development Tools

* VS Code
* Git
* GitHub

---

## System Workflow

```text
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
      ┌─────────────────┐              ┌─────────────────┐
      │ Upload Resume   │              │ Enter Job       │
      │                 │              │ Description     │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               └──────────────┬─────────────────┘
                              ▼
                   ┌─────────────────────┐
                   │ Text Preprocessing  │
                   │ & NLP Processing     │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Feature Extraction  │
                   │ / Text Embeddings   │
                   └──────────┬──────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
       ┌─────────────────┐         ┌─────────────────┐
       │ Resume–Job      │         │ Fake Job        │
       │ Matching        │         │ Detection       │
       └────────┬────────┘         └────────┬────────┘
                │                           │
                └─────────────┬─────────────┘
                              ▼
                   ┌─────────────────────┐
                   │ Analysis & Results  │
                   └─────────────────────┘
```

---

## Fake Job Detection Methodology

The fake job detection module uses a supervised machine learning approach.

### Step 1: Data Collection

A dataset containing job postings labeled as legitimate or fraudulent is used for model training.

### Step 2: Text Preprocessing

Job-related text is cleaned and processed using NLP techniques such as:

* Lowercasing
* Removing unnecessary characters
* Tokenization
* Stop-word removal
* Text normalization

### Step 3: Feature Extraction

The processed text is converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

### Step 4: Model Training

A **Logistic Regression classifier** is trained using the extracted features.

### Step 5: Prediction

When a new job posting is submitted, the trained model analyzes the text and predicts whether the posting is:

```text
Legitimate Job
       OR
Potentially Fake Job
```

---

## Resume Analysis Methodology

The resume analysis module processes the uploaded resume and compares it with the target job description.

### Resume Processing

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill / Keyword Extraction
      ↓
Text Representation
      ↓
Comparison with Job Description
      ↓
Compatibility Analysis
```

The system can identify relevant keywords and skills and use text similarity/embedding-based techniques to determine how closely the resume matches the job requirements.

---

## ⚙️ Installation


### 1. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Open the application in your browser using the local URL displayed by the server.


---

## Model Evaluation

The fake job detection model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

For a fraud-detection problem, **accuracy alone should not be treated as sufficient**. Precision, recall, and F1-score are important for understanding how well the model identifies fraudulent postings without incorrectly flagging legitimate jobs.

---

## Security Considerations

The application should consider:

* File type validation for uploaded resumes.
* File size restrictions.
* Input validation.
* Sanitization of user-provided text.
* Secure handling of uploaded documents.
* Avoiding storage of unnecessary personal information from resumes.

---

## Future Enhancements

Possible improvements include:

* ATS-style resume scoring.
* Advanced skill extraction using Named Entity Recognition.
* More sophisticated semantic similarity models.
* Support for multiple resume formats.
* Explainable AI for fake-job predictions.
* Job recommendation based on resume skills.
* Resume improvement suggestions.
* LinkedIn/job-portal integration.
* Cloud deployment.
* Authentication and user profiles.
* Dashboard with analytics.
* Improved fraud detection using additional job-posting metadata.

---

## Use Cases

### For Job Seekers

* Analyze resume quality.
* Compare resume with job descriptions.
* Identify missing skills.
* Detect suspicious job postings before applying.

### For Recruiters

* Quickly evaluate candidate resumes.
* Compare candidates with job requirements.
* Automate initial resume screening.

### For Students

* Understand ATS and resume matching.
* Learn practical NLP and Machine Learning.
* Build experience with REST APIs and web application deployment.

---

## Project Highlights

* Combines **Machine Learning + NLP + Web Development** in one application.
* Uses **TF-IDF and Logistic Regression** for text classification.
* Uses **text similarity / embeddings** for resume–job matching.
* Provides an API-based backend.
* Demonstrates an end-to-end ML application workflow.
* Addresses a practical problem faced by job seekers and recruiters.

---

## Skills Demonstrated

```text
Python
Machine Learning
Natural Language Processing
Text Classification
TF-IDF
Logistic Regression
Text Embeddings
Semantic Similarity
Scikit-learn
Flask
HTML
CSS
JavaScript
Git & GitHub
Model Deployment
```

---

## 👩‍💻 Author

**Shravani Jadhav**

B.Tech Computer Science & Engineering


## If You Like This Project

If you find this project useful, consider giving the repository a on GitHub.
