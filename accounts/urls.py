from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('dashboard/', views.dashboard, name='dashboard'),

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

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset-password/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url='/accounts/reset-password/complete/'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset-password/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]