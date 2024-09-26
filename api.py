from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from sum import another_sum

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define a request model using Pydantic
class SumRequest(BaseModel):
    number_string: str

# Endpoint to handle sum calculation
@app.post("/calculate_sum")
async def calculate_sum(request: SumRequest):
    try:
        # Initialize Sum object with the input string from the request
        sum_calculator = another_sum.Sum(request.number_string)
        
        # Calculate the sum of valid numbers
        result = sum_calculator.another_sum()

        # Return the result as JSON
        return {"sum": result}
    
    except ValueError as e:
        # Handle cases where there are negative numbers or other issues
        raise HTTPException(status_code=400, detail=str(e))

