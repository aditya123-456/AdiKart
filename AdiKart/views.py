from django.shortcuts import render
from store.models import product
from category.models import Category


def home(request):
    products = product.objects.all().filter(is_available=True)
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'products': products,
        'categories': categories,
    })

