
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # Registration
    path(
        'register/',
        views.register,
        name='register'
    ),

    # Login and Logout
    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # Email Activation
    path(
        'activate/<uidb64>/<token>/',
        views.activate,
        name='activate'
    ),

    # Customer Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # My Orders
    path(
        'my-orders/',
        views.my_orders,
        name='my_orders'
    ),

    # Order Invoice
    path(
        'order-invoice/<int:order_id>/',
        views.order_invoice,
        name='order_invoice'
    ),

    # Edit Profile
    path(
        'edit-profile/',
        views.edit_profile,
        name='edit_profile'
    ),

    # Change Password
    path(
        'change-password/',
        views.change_password,
        name='change_password'
    ),

    # Forgot Password
    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/forgot_password.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt',
            success_url='/accounts/forgot-password/done/'
        ),
        name='forgot_password'
    ),

    # Password Reset Email Sent
    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Reset Password
    path(
        'reset-password/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url='/accounts/reset-password/complete/'
        ),
        name='password_reset_confirm'
    ),

    # Password Reset Complete
    path(
        'reset-password/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]
