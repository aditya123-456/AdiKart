from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

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
            is_active=False,
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
            to=[email],
        )

        email_message.send()

        return render(
            request,
            'accounts/account_activation_sent.html'
        )

    return render(request, 'accounts/register.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
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


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

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

            return redirect('home')

        return render(request, 'accounts/login.html', {
            'error': 'Invalid email or password'
        })

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    from orders.models import Order

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'accounts/dashboard.html', {
        'orders': orders,
    })