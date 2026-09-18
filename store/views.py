from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import product
from category.models import Category


def store(request):
    products = product.objects.all()
    categories = Category.objects.all()

    keyword = request.GET.get('keyword')

    if keyword:
        products = products.filter(
            Q(product_name__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(category__category_name__icontains=keyword)
        )

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    product_count = paginator.count

    return render(request, 'store/store.html', {
        'products': products,
        'categories': categories,
        'product_count': product_count,
        'keyword': keyword,
    })


def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    products = product.objects.filter(category=category)
    categories = Category.objects.all()

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    product_count = paginator.count

    return render(request, 'store/store.html', {
        'products': products,
        'categories': categories,
        'product_count': product_count,
    })


def product_detail(request, product_slug):
    product_item = get_object_or_404(product, slug=product_slug)

    return render(request, 'store/product-detail.html', {
        'product': product_item,
    })
# Create your views here.
