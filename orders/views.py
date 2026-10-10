
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .models import Order, OrderProduct
from store.models import product


@login_required
@require_http_methods(["GET", "POST"])
def checkout(request):
    cart_data = request.session.get('cart', {})

    if not cart_data:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart')

    cart_items = []
    total = 0

    for cart_key, data in cart_data.items():
        item = get_object_or_404(
            product,
            id=data['product_id']
        )

        quantity = int(data['quantity'])
        subtotal = item.price * quantity
        total += subtotal

        cart_items.append({
            'product': item,
            'quantity': quantity,
            'color': data.get('color', ''),
            'size': data.get('size', ''),
            'subtotal': subtotal,
        })

    tax = round(total * 0.10, 2)
    shipping_fee = 50
    grand_total = round(total + tax + shipping_fee, 2)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            phone=request.POST.get('phone', ''),
            email=request.POST.get('email', ''),
            address=request.POST.get('address', ''),
            city=request.POST.get('city', ''),
            state=request.POST.get('state', ''),
            pincode=request.POST.get('pincode', ''),
            order_total=total,
            tax=tax,
            shipping_fee=shipping_fee,
            grand_total=grand_total,
            payment_method=request.POST.get(
                'payment_method', 'Cash on Delivery'
            ),
            status='New',
        )

        for item in cart_items:
            OrderProduct.objects.create(
                order=order,
                user=request.user,
                product=item['product'],
                quantity=item['quantity'],
                product_price=item['product'].price,
                color=item['color'],
                size=item['size'],
            )

        # Clear cart after saving the order.
        request.session['cart'] = {}
        request.session.modified = True

        return redirect(
            'order_confirmation',
            order_id=order.id
        )

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'shipping_fee': shipping_fee,
        'grand_total': grand_total,
    })


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order_products = OrderProduct.objects.filter(
        order=order
    )

    return render(request, 'orders/order_confirmation.html', {
        'order': order,
        'order_products': order_products,
    })


@login_required
def demo_payment_success(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order_products = OrderProduct.objects.filter(
        order=order
    )

    # Demonstration only. No real payment is processed.
    # Do not mark the order as paid.
    return render(
        request,
        'orders/payment_success.html',
        {
            'order': order,
            'order_products': order_products,
        }
    )
