from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from calculator.forms import CalculatorForm
from calculator.models import Calculation

def home(request):
    return render(request, 'calculator/home.html')

@login_required
def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = eval(expression)  # Be cautious with eval
                Calculation.objects.create(
                    user=request.user,
                    expression=expression,
                    result=result
                )
                return render(request, 'calculator/calculator.html', {
                    'form': form,
                    'result': result
                })
            except Exception as e:
                return render(request, 'calculator/calculator.html', {
                    'form': form,
                    'error': str(e)
                })
    else:
        form = CalculatorForm()
    return render(request, 'calculator/calculator.html', {'form': form})

@login_required
def history(request):
    calculations = Calculation.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'calculator/history.html', {'calculations': calculations})
