from django.conf import settings
from django.db import models


class ReviewRating(models.Model):
    product = models.ForeignKey(
        'store.Product',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    review_title = models.CharField(max_length=150)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.review_title} - {self.product.product_name}'