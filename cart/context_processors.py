def cart_count(request):

    cart = request.session.get('cart', {})

    count = 0

    for data in cart.values():

        if isinstance(data, dict):
            count += data.get('quantity', 0)
        else:
            count += data

    return {
        'cart_count': count
    }