from django.db import models
from accounts.models import Account
from store.models import product


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    shipping_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(max_length=50)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"

    @property
    def order_number(self):
        return f"ORDER-{self.id}"


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    color = models.CharField(
        max_length=50,
        blank=True
    )

    size = models.CharField(
        max_length=50,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product.product_name