from fastapi import APIRouter

router = APIRouter()

@router.post("/calculate")
def sum_numbers(num1: int, num2: int):
    return {"result": num1+num2}

