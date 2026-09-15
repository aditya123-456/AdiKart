from django.shortcuts import render, get_object_or_404
from .models import product
from category.models import Category

def store(request, category_slug=None):
    products = product.objects.all()
    categories = Category.objects.all()

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = product.objects.filter(category=category)

    product_count = products.count()

    return render(request, 'store/store.html', {
        'products': products,
        'categories': categories,
        'product_count': product_count,
    })


def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(
        product,
        category__slug=category_slug,
        slug=product_slug
    )

    return render(request, 'store/product_detail.html', {
        'single_product': single_product,
    })
# Create your views here.
