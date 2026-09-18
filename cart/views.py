from django.shortcuts import render, redirect, get_object_or_404
from store.models import product


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('cart')


def cart(request):
    cart_data = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():
        item = get_object_or_404(product, id=product_id)

        subtotal = item.price * quantity
        total += subtotal

        cart_items.append({
            'product': item,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    tax = total * 0.10
    grand_total = total + tax

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')