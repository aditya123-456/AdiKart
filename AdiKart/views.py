from django.shortcuts import render
from store.models import product

def home(request):
    products = product.objects.all()
    return render(request, 'home.html', {'products': products})

