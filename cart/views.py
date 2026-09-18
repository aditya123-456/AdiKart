from django.shortcuts import render, redirect, get_object_or_404
from store.models import product


def add_to_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    color = request.GET.get('color', 'Green')
    size = request.GET.get('size', 'Medium')

    cart_key = f"{product_id}_{color}_{size}"

    if cart_key in cart:
        cart[cart_key]['quantity'] += 1
    else:
        cart[cart_key] = {
            'product_id': product_id,
            'color': color,
            'size': size,
            'quantity': 1,
        }

    request.session['cart'] = cart

    return redirect('cart')


def cart(request):

    cart_data = request.session.get('cart', {})

    cart_items = []

    total = 0

    for cart_key, data in cart_data.items():

        item = get_object_or_404(
            product,
            id=data['product_id']
        )

        quantity = data['quantity']

        subtotal = item.price * quantity

        total += subtotal

        cart_items.append({
            'product': item,
            'quantity': quantity,
            'color': data['color'],
            'size': data['size'],
            'subtotal': subtotal,
            'cart_key': cart_key,
        })

    tax = total * 0.10

    grand_total = total + tax

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    })


def remove_from_cart(request, cart_key):

    cart = request.session.get('cart', {})

    if cart_key in cart:
        del cart[cart_key]

    request.session['cart'] = cart

    return redirect('cart')


def increase_quantity(request, cart_key):

    cart = request.session.get('cart', {})

    if cart_key in cart:
        cart[cart_key]['quantity'] += 1

    request.session['cart'] = cart

    return redirect('cart')


def decrease_quantity(request, cart_key):

    cart = request.session.get('cart', {})

    if cart_key in cart:

        if cart[cart_key]['quantity'] > 1:
            cart[cart_key]['quantity'] -= 1
        else:
            del cart[cart_key]

    request.session['cart'] = cart

    return redirect('cart')