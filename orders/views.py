from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderProduct
from store.models import product


@login_required
def checkout(request):
    cart_data = request.session.get('cart', {})

    if not cart_data:
        return redirect('cart')

    cart_items = []
    total = 0

    for cart_key, data in cart_data.items():
        item = product.objects.get(id=data['product_id'])

        quantity = data['quantity']
        subtotal = item.price * quantity
        total += subtotal

        cart_items.append({
            'product': item,
            'quantity': quantity,
            'color': data['color'],
            'size': data['size'],
            'subtotal': subtotal,
        })

    tax = total * 0.10
    shipping_fee = 50
    grand_total = total + tax + shipping_fee

    if request.method == 'POST':

        order = Order.objects.create(
            user=request.user,
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            pincode=request.POST['pincode'],
            order_total=total,
            tax=tax,
            shipping_fee=shipping_fee,
            grand_total=grand_total,
            payment_method=request.POST['payment_method'],
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

        request.session['cart'] = {}

        return redirect('dashboard')

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'shipping_fee': shipping_fee,
        'grand_total': grand_total,
    })