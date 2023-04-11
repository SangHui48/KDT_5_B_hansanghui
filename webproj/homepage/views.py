from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
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
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/coffees')
    form = CoffeeForm()
    return render(
        request,
        'coffee_form.html',
        {
            "coffee_form": form
        }
    )

def update_coffee(request, id):
    coffee = get_object_or_404(Coffee, pk=id)
    if request.method == 'POST':
        form = CoffeeForm(request.POST, instance=coffee)
        if form.is_valid():
            form.save()
            return redirect('/coffees')
    else:
        form = CoffeeForm(instance=coffee)

    return render(
        request,
        'coffee_update.html',
        {
            'form': form
        }
    )