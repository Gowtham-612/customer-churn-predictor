from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.schema.user_input import CustomerData
from app.models.predict import predict_churn, MODEL_VERSION
from app.schema.prediction_response import PredictionResponse
import os
import uvicorn

app = FastAPI(title="Customer Churn Prediction API")



@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Churn Prediction API!"}

@app.post("/predict", response_model=PredictionResponse)
def churn_prediction(data: CustomerData):
    # Convert input data to DataFrame
    input_df = {
        "CreditScore": data.CreditScore,
        "Geography": data.Geography,
        "Gender": data.Gender,
        "Age": data.Age,
        "Tenure": data.Tenure,
        "Balance": data.Balance,
        "NumOfProducts": data.NumOfProducts,
        "HasCrCard": data.HasCrCard,
        "IsActiveMember": data.IsActiveMember,
        "EstimatedSalary": data.EstimatedSalary
    }

    # Preprocess the input data
   
    try:
      prediction = predict_churn(input_df)
      return prediction
    except Exception as e:
      return JSONResponse(content={"error": str(e)}, status_code=500)
    


@app.get("/health")
def health_check():
    return {"status": "API is healthy"
            , "model_version": MODEL_VERSION} 

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
    )