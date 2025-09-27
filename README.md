# Customer Support Ticket Auto-Triage Project

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![ML Library](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

This project is a complete solution for automatically classifying customer support tickets using Natural Language Processing and Machine Learning, fulfilling the requirements of the AI/ML Assessment.

---

### Table of Contents
1.  [Project Objective](#project-objective)
2.  [Dataset Selection and Usage](#dataset-selection-and-usage)
3.  [Model and Data Access](#model-and-data-access)
4.  [Technical Stack](#technical-stack)
5.  [Project Structure](#project-structure)
6.  [Setup and Installation](#setup-and-installation)
7.  [Execution Workflow](#execution-workflow)
8.  [How to Use the API](#how-to-use-the-api)
9.  [Model Performance](#model-performance)

---

### ## Project Objective
The core mission of this project is to enhance operational efficiency by automating the initial classification of customer support tickets. A machine learning pipeline processes ticket descriptions to predict a category, allowing for intelligent routing to the most appropriate team, thereby reducing manual effort and accelerating resolution times.

---

### ## Dataset Selection and Usage
The project brief outlined the *structure* of a dataset but did not provide a data file. To build a robust, real-world solution, an external dataset was required.

#### **Why was this dataset chosen?**
The **Consumer Complaint Database** from the Consumer Financial Protection Bureau (CFPB), available on Kaggle, was selected for the following reasons:
* **Relevance:** It contains hundreds of thousands of real customer complaints, which is a perfect proxy for customer support tickets.
* **Rich Text Data:** The `consumer_complaint_narrative` field provides substantial text for training a powerful NLP model.
* **Pre-existing Labels:** The `product` column serves as a reliable target variable for classification.
* **Scale:** Its large size is ideal for training a model that generalizes well.

#### **How were the columns used?**
The columns from the Kaggle dataset were mapped to the project requirements as follows:
* `product` ➡️ **Category** (The target variable for our classifier).
* `consumer_complaint_narrative` ➡️ **Description** (The primary text feature used for training).
* `complaint_id` ➡️ **Ticket ID** (The unique identifier).
* `date_received` ➡️ **Timestamp** (The creation date).

The `Subject` and `Priority` fields from the original spec were not present in this dataset and were excluded to focus on the core classification task based on the ticket's content.

---

### ## Model and Data Access
As per the submission guidelines, the final model and the dataset must be accessible. Since these files are too large for a Git repository, they are hosted externally:

* **Download the Dataset (`complaints.csv`):** [**Click here to download from Kaggle**](https://www.kaggle.com/datasets/cfpb/us-consumer-finance-complaints)
* **Download the Trained Model (`support_ticket_classifier.joblib`):** [**[Paste your Google Drive, Dropbox, or other shareable link here](https://drive.google.com/drive/folders/1ibqEOzaOJbfnokW4TApuRcc-KwIDfwuJ?usp=sharing)**]

---

### ## Technical Stack
* **Python 3.8+**
* **Machine Learning**: Scikit-Learn (for modeling, pipelines, and feature extraction)
* **API Framework**: FastAPI (for serving the model)
* **NLP**: NLTK (for text preprocessing)
* **Data Handling**: Pandas, NumPy
* **Web Server**: Uvicorn

---



### ## Project Showcase

#### **1. Uvicorn Server Running in Terminal**
![Uvicorn Server Running](<images/uvicorn.png>)

#### **2. API Endpoint Test via Interactive Docs**
![FastAPI Docs Test](<images/api.png>)

---

### ## Project Structure
```
suppor-ticket-classifier/
│
├── .gitignore              # Specifies files for Git to ignore
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── support_ticket_classifier.joblib # The final trained model pipeline
│
├── data/                   # (Should be created by the user to store complaints.csv)
│
├── notebooks/
│   ├── 1_Data_Preprocessing_and_EDA.ipynb
│   └── 2_Model_Training_and_Tuning.ipynb
│
├── processed_data/         # Saved intermediate files (not in Git)
│
└── src/
    ├── __init__.py
    └── main.py             # The FastAPI application
```
---

### ## Setup and Installation
1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd suppor-ticket-classifier
    ```
2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
---
### ## Execution Workflow
Follow these steps to reproduce the model and run the application.

1.  **Download Data:** Download `complaints.csv` from the link in the [Model and Data Access](#model-and-data-access) section and place it in a newly created `data/` folder in the project root.

2.  **Run Jupyter Notebooks:** Open the `notebooks/` directory and run the notebooks in order:
    * `1_Data_Preprocessing_and_EDA.ipynb`: This will perform initial analysis and text cleaning.
    * `2_Model_Training_and_Tuning.ipynb`: This will train the final model and save `support_ticket_classifier.joblib` in the root directory.

3.  **Run the API Server:**
    From the root directory, start the FastAPI server:
    ```bash
    uvicorn src.main:app --reload
    ```
---

### ## How to Use the API
The API will be available at `http://122.0.0.1:8000`.

#### **Interactive Docs (Recommended)**
Navigate to `http://122.0.0.1:8000/docs` in your browser to access the interactive Swagger UI for easy testing.

#### **cURL Example**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "description": "My mortgage application status has not been updated in weeks."
}'
```
**Expected Response:**
```json
{"predicted_category": "Mortgage"}
```
---

### ## Model Performance
The final model is a Scikit-Learn `Pipeline` containing a `TfidfVectorizer` and a tuned `LogisticRegression` classifier. It achieved the following performance on the hold-out test set:

* **Accuracy:** 89.4%
* **Macro Avg F1-Score:** 0.88


