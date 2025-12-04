
import pickle
import pandas as pd
import joblib
from tensorflow.keras.models import load_model


MODEL_VERSION = "0.0.1"

# Load saved components
preprocessor = joblib.load("models/preprocessor1.joblib")
model = load_model("models/ann_model1.h5")



def predict_churn(data: dict) -> dict:
     # Convert input data to DataFrame
     input_df = pd.DataFrame([data])
 
     # Preprocess the input data
     processed_data = preprocessor.transform(input_df)
 
     # Make prediction
     prediction = model.predict(processed_data)
     churn_probability = prediction[0][0]
     churn_prediction = int(churn_probability > 0.5)    

     return {
         "churn_prediction": churn_prediction,
         "churn_probability": float(churn_probability)
     }
 
     # Return prediction result