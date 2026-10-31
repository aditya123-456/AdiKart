
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import product, ReviewRating
from category.models import Category
from orders.models import OrderProduct


def store(request):

    products = product.objects.filter(is_available=True)

    return render(request, 'store/store.html', {
        'products': products
    })


def products_by_category(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    products = product.objects.filter(
        category=category,
        is_available=True
    )

    return render(request, 'store/store.html', {
        'products': products,
        'category': category
    })


def product_detail(request, product_slug):

    product_item = get_object_or_404(
        product,
        slug=product_slug
    )

    reviews = ReviewRating.objects.filter(
        product=product_item,
        status=True
    ).select_related('user')

    can_review = False

    if request.user.is_authenticated:

        can_review = OrderProduct.objects.filter(
            user=request.user,
            product=product_item,
            order__payment_status='Success'
        ).exists()

    return render(
        request,
        'store/product-detail.html',
        {
            'product': product_item,
            'reviews': reviews,
            'can_review': can_review,
        }
    )


@login_required
def submit_review(request, product_id):

    if request.method != 'POST':
        return redirect('store')

    product_item = get_object_or_404(
        product,
        id=product_id
    )

    # Verify successful payment for this exact product.
    purchased = OrderProduct.objects.filter(
        user=request.user,
        product=product_item,
        order__payment_status='Success'
    ).exists()

    if not purchased:

        messages.error(
            request,
            'You can review this product only after purchasing it.'
        )

        return redirect(
            'product_detail',
            product_slug=product_item.slug
        )

    try:
        rating = int(request.POST.get('rating', 0))
    except (TypeError, ValueError):
        rating = 0

    review_title = request.POST.get(
        'review_title', ''
    ).strip()

    review_text = request.POST.get(
        'review', ''
    ).strip()

    if not 1 <= rating <= 5:

        messages.error(
            request,
            'Please select a rating between 1 and 5.'
        )

    elif not review_title or not review_text:

        messages.error(
            request,
            'Please enter both review title and review.'
        )

    else:

        ReviewRating.objects.create(
            product=product_item,
            user=request.user,
            review_title=review_title,
            review=review_text,
            rating=rating,
            status=True
        )

        messages.success(
            request,
            'Your review was submitted successfully!'
        )

    return redirect(
        'product_detail',
        product_slug=product_item.slug
    )
