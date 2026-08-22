# AI-Powered Resume Analyzer & Fake Job Detection System

An AI-powered web application that analyzes resumes, evaluates resume–job compatibility, and detects potentially fraudulent or fake job postings using Natural Language Processing (NLP) and Machine Learning.

## 📌 Project Overview

The AI-Powered Resume Analyzer & Fake Job Detection System combines two recruitment-related capabilities into a single platform:

1. Resume Analysis & Job Matching – analyzes a candidate's resume against a job description and identifies relevant skills, keywords, and compatibility.

2. Fake Job Detection – analyzes job postings and predicts whether they are likely to be legitimate or fraudulent.

The system uses Natural Language Processing, Machine Learning, and text similarity techniques to automate parts of the recruitment and job-search process.

---

## 🚀 Key Features

### 📄 Resume Analyzer

* Upload and analyze resumes.
* Extract important information from resume text.
* Identify technical skills and relevant keywords.
* Compare resume content with a given job description.
* Calculate resume–job compatibility.
* Highlight relevant or missing skills.
* Provide AI-based analysis of the candidate profile.

### 🛡️ Fake Job Detection

* Analyze job titles and descriptions.
* Detect suspicious or potentially fraudulent job postings.
* Use NLP-based text processing and machine learning for classification.
* Predict whether a job posting appears legitimate or suspicious.
* Provide analysis based on textual characteristics of the job posting.

### 💻 User-Friendly Interface

* Simple web-based interface.
* Resume upload functionality.
* Job description input.
* Prediction and analysis results.
* Easy-to-understand output.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning & NLP

* NLTK
* Scikit-learn
* Pandas
* NumPy
* TF-IDF Vectorization
* Logistic Regression
* Sentence Transformers / Text Embeddings

### Backend

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

## 🔄 System Workflow

```text
                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
      ┌─────────────────┐              ┌─────────────────┐
      │  Upload Resume  │              │  Enter Job      │
      │                 │              │  Description     │
      └────────┬────────┘              └────────┬────────┘
               │                                │
               └──────────────┬─────────────────┘
                              ▼
                   ┌─────────────────────┐
                   │ Text Preprocessing  │
                   │ & NLP Processing    │
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

## 🔍 Fake Job Detection Methodology

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

The processed text is converted into numerical features using TF-IDF (Term Frequency–Inverse Document Frequency).

### Step 4: Model Training

A Logistic Regression classifier is trained using the extracted features.

### Step 5: Prediction

When a new job posting is submitted, the trained model analyzes the text and predicts whether the posting is:

```text
Legitimate Job

       OR

Potentially Fake Job
```

---

## 📄 Resume Analysis Methodology

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

The system identifies relevant keywords and skills and uses text similarity or embedding-based techniques to determine how closely the resume matches the job requirements.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <(https://github.com/shravanijadhav264/JobShieldAI)>
```

```bash
cd JobShieldAI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open the local URL displayed in the terminal to access the application.

---

## 📊 Model Evaluation

The fake job detection model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

For a fraud-detection problem, accuracy alone is not sufficient. Precision, recall, and F1-score are important for understanding how effectively the model identifies fraudulent postings while minimizing incorrect classifications.

---

## 🔐 Security Considerations

The application should consider:

* File type validation for uploaded resumes.
* File size restrictions.
* Input validation.
* Sanitization of user-provided text.
* Secure handling of uploaded documents.
* Avoiding unnecessary storage of personal information from resumes.

---

## 🔮 Future Enhancements

* ATS-style resume scoring.
* Advanced skill extraction using Named Entity Recognition.
* More sophisticated semantic similarity models.
* Support for multiple resume formats.
* Explainable AI for fake-job predictions.
* Job recommendations based on resume skills.
* Resume improvement suggestions.
* Job portal integration.
* Cloud deployment.
* Authentication and user profiles.
* Analytics dashboard.
* Improved fraud detection using additional job-posting metadata.

---

## 🎯 Use Cases

### For Job Seekers

* Analyze resume quality.
* Compare resumes with job descriptions.
* Identify missing skills.
* Detect suspicious job postings before applying.

### For Recruiters

* Quickly evaluate candidate resumes.
* Compare candidates with job requirements.
* Automate initial resume screening.

### For Students

* Learn practical applications of NLP and Machine Learning.
* Understand resume–job matching.
* Gain experience building and deploying ML-powered web applications.

---

## ⭐ Project Highlights

* Combines **Machine Learning, NLP, and Web Development** in one application.
* Uses **TF-IDF and Logistic Regression** for fake-job text classification.
* Uses **text similarity and embeddings** for resume–job matching.
* Provides a web-based interface for interacting with the models.
* Demonstrates an end-to-end machine learning application workflow.
* Addresses a practical problem faced by job seekers and recruiters.

---

## 💡 Skills Demonstrated

```text
Python
Machine Learning
Natural Language Processing
Text Classification
TF-IDF
Logistic Regression
Text Embeddings
Semantic Similarity
Pandas
NumPy
Scikit-learn
NLTK
Flask
HTML
CSS
JavaScript
Bootstrap
Git
GitHub
Model Deployment
```

---

## 👩‍💻 Author

Shravani Jadhav

B.Tech Computer Science & Engineering

---

