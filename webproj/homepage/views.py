from django.shortcuts import render, HttpResponse
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def coffee_view(request):
    coffee_all = Coffee.objects.all()
    return render(
        request,
        'coffee.html',
        {
        'coffee_list': coffee_all
        }
    )

def register_coffee(request):
    form = CoffeeForm()
    return render(
        request,
        'coffee_form.html',
        {
            "coffee_form": form
        }
    )