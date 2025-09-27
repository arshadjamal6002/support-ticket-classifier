# Customer Support Ticket Auto-Triage

## Project Objective

This project aims to enhance operational efficiency by automating the classification of customer support tickets. It uses a machine learning model to categorize tickets into predefined groups, enabling them to be routed to the correct team automatically.

---

## Technical Stack
- **Python 3.8+**
- **Machine Learning**: Scikit-Learn
- **API**: FastAPI
- **NLP**: NLTK

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd suppor-ticket-classifier
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run the API

To start the API server, run the following command from the root project directory:

```bash
uvicorn src.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## How to Use the API

You can interact with the API through the auto-generated documentation at `http://127.0.0.1:8000/docs`.

Alternatively, you can send a `POST` request using a tool like `curl`:

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
{
  "predicted_category": "Mortgage"
}
```