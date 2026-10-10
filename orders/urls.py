from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),

    path(
        'confirmation/<int:order_id>/',
        views.order_confirmation,
        name='order_confirmation'
    ),

    path(
        'demo-payment-success/<int:order_id>/',
        views.demo_payment_success,
        name='demo_payment_success'
    ),
]


