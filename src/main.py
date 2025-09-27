import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the FastAPI app
app = FastAPI(title="Customer Support Ticket Classifier API")

# 2. Load the trained pipeline
try:
    model = joblib.load('C:\\Users\\arsha\\Downloads\\suppor-ticket-classifier\\support_ticket_classifier.joblib')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: Model file not found. Make sure 'support_ticket_classifier.joblib' is in the root directory.")
    model = None

# 3. Define the request body structure using Pydantic
class Ticket(BaseModel):
    description: str

# 4. Define the prediction endpoint
@app.post("/predict")
def predict_category(ticket: Ticket):
    """
    Receives ticket description and returns the predicted category.
    """
    if model is None:
        return {"error": "Model not loaded. Please check server logs."}
        
    # The input to predict must be an iterable (like a list)
    prediction = model.predict([ticket.description])
    
    # Return the prediction in a JSON response
    return {"predicted_category": prediction[0]}

# 5. Define a root endpoint for health checks
@app.get("/")
def read_root():
    return {"status": "API is running."}