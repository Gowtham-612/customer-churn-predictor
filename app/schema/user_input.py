
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated


class CustomerData(BaseModel):
    CreditScore:Annotated[int, Field(gt=0, description="Customer's credit score")]
    Geography:Annotated[Literal['France', 'Spain', 'Germany'], Field(description="Customer's country")]
    Gender:Annotated[Literal['Male', 'Female'], Field(description="Customer's gender")]    
    Age:Annotated[int, Field(gt=0, description="Customer's age")]
    Tenure:Annotated[int, Field(ge=0, description="Number of years the customer has been with the bank")]
    Balance:Annotated[float, Field(ge=0, description="Customer's account balance")]
    NumOfProducts:Annotated[int, Field(ge=1, description="Number of bank products the customer is using")]
    HasCrCard:Annotated[int, Field(ge=0, le=1, description="Whether the customer has a credit card (1) or not (0)")]
    IsActiveMember:Annotated[int, Field(ge=0, le=1, description="Whether the customer is an active member (1) or not (0)")]
    EstimatedSalary:Annotated[float, Field(ge=0, description="Customer's estimated salary")]
