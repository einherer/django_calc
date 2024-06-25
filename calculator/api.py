from ninja import NinjaAPI
from calculator.models import Calculation, UserProfile
from django.contrib.auth.models import User
from ninja import Schema
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class CalculationSchema(Schema):
    expression: str
    result: float

@api.post("/calculate")
def calculate(request, expression: str):
    try:
        result = eval(expression)
        calculation = Calculation.objects.create(
            user=request.user,
            expression=expression,
            result=result
        )
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"error": str(e)}

@api.get("/history", response=list[CalculationSchema])
def history(request):
    user = request.user
    calculations = Calculation.objects.filter(user=user)
    return calculations
