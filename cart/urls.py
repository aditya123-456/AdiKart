from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<str:cart_key>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase/<str:cart_key>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<str:cart_key>/', views.decrease_quantity, name='decrease_quantity'),
]