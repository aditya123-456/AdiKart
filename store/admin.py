
from django.contrib import admin
from .models import ReviewRating


@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):

    list_display = (
        'review_title',
        'product',
        'user',
        'rating',
        'created_at',
    )

    list_filter = ('rating', 'created_at')

    search_fields = (
        'review_title',
        'review',
    )

    ordering = ('-created_at',)
