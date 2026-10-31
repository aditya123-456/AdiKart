
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordChangeForm

from .models import Account


# ==========================================
# USER REGISTRATION
# ==========================================

def register(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            return render(request, 'accounts/register.html', {
                'error': 'Passwords do not match'
            })

        if Account.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Email already exists'
            })

        user = Account(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            username=email,
            is_active=False
        )

        user.set_password(password)
        user.save()

        current_site = get_current_site(request)

        mail_subject = 'Activate your AdiKart account'

        message = render_to_string(
            'accounts/account_activation_email.html',
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }
        )

        email_message = EmailMessage(
            mail_subject,
            message,
            to=[email]
        )

        email_message.send()

        return render(
            request,
            'accounts/account_activation_sent.html'
        )

    return render(request, 'accounts/register.html')


# ==========================================
# ACCOUNT ACTIVATION
# ==========================================

def activate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(pk=uid)

    except (
        TypeError,
        ValueError,
        OverflowError,
        Account.DoesNotExist
    ):
        user = None

    if user is not None and default_token_generator.check_token(user, token):

        user.is_active = True
        user.save()

        return render(
            request,
            'accounts/account_activated.html'
        )

    return render(
        request,
        'accounts/account_activation_invalid.html'
    )


# ==========================================
# USER LOGIN
# ==========================================

def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            if not user.is_active:
                return render(request, 'accounts/login.html', {
                    'error': 'Please activate your account first'
                })

            login(request, user)

            return redirect('dashboard')

        return render(request, 'accounts/login.html', {
            'error': 'Invalid email or password'
        })

    return render(request, 'accounts/login.html')


# ==========================================
# USER LOGOUT
# ==========================================

@login_required
def logout_view(request):

    logout(request)

    return redirect('home')


# ==========================================
# CUSTOMER DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    from orders.models import Order

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        'orders': orders[:5],
        'total_orders': orders.count(),
    }

    return render(
        request,
        'accounts/dashboard.html',
        context
    )


# ==========================================
# MY ORDER HISTORY
# ==========================================

@login_required
def my_orders(request):

    from orders.models import Order

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'accounts/my_orders.html',
        {
            'orders': orders,
        }
    )


# ==========================================
# ORDER INVOICE
# ==========================================

@login_required
def order_invoice(request, order_id):

    from orders.models import Order, OrderProduct

    # Only allow customers to view their own orders.
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order_products = OrderProduct.objects.filter(
        order=order
    ).select_related('product')

    context = {
        'order': order,
        'order_products': order_products,
    }

    return render(
        request,
        'accounts/order_invoice.html',
        context
    )


# ==========================================
# EDIT CUSTOMER PROFILE
# ==========================================

@login_required
def edit_profile(request):

    if request.method == 'POST':

        first_name = request.POST.get(
            'first_name', ''
        ).strip()

        last_name = request.POST.get(
            'last_name', ''
        ).strip()

        phone_number = request.POST.get(
            'phone_number', ''
        ).strip()

        address_line_1 = request.POST.get(
            'address_line_1', ''
        ).strip()

        address_line_2 = request.POST.get(
            'address_line_2', ''
        ).strip()

        city = request.POST.get(
            'city', ''
        ).strip()

        state = request.POST.get(
            'state', ''
        ).strip()

        country = request.POST.get(
            'country', ''
        ).strip()

        profile_picture = request.FILES.get('profile_picture')

        if not first_name or not last_name or not phone_number:

            messages.error(
                request,
                'Please fill in your name and phone number.'
            )

        else:

            user = request.user

            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number

            user.address_line_1 = address_line_1
            user.address_line_2 = address_line_2
            user.city = city
            user.state = state
            user.country = country

            if profile_picture:
                user.profile_picture = profile_picture

            user.save()

            messages.success(
                request,
                'Your profile was updated successfully!'
            )

            return redirect('edit_profile')

    return render(
        request,
        'accounts/edit_profile.html'
    )


# ==========================================
# CHANGE PASSWORD
# ==========================================

@login_required
def change_password(request):

    if request.method == 'POST':

        form = PasswordChangeForm(
            user=request.user,
            data=request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                'Your password was changed successfully!'
            )

            return redirect('change_password')

        messages.error(
            request,
            'Please correct the errors below.'
        )

    else:

        form = PasswordChangeForm(
            user=request.user
        )

    return render(
        request,
        'accounts/change_password.html',
        {
            'form': form
        }
    )

