from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated

class PredictionResponse(BaseModel):
    churn_prediction: Annotated[int, Field(description="Predicted churn status: 1 for churn, 0 for no churn")]
    churn_probability: Annotated[float, Field(ge=0, le=1, description="Predicted probability of churn")]
 