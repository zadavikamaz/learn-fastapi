from fastapi import APIRouter

calculate = APIRouter()

@calculate.post("/calculate")
async def sum_numbers(num1: int, num2: int):
    return {"result": num1+num2}

