
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),

    path(
        'product/<slug:product_slug>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'submit-review/<int:product_id>/',
        views.submit_review,
        name='submit_review'
    ),

    path(
        'category/<slug:category_slug>/',
        views.products_by_category,
        name='products_by_category'
    ),
]

