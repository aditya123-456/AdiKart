from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'email',
        'order_total',
        'grand_total',
        'status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = ('id', 'email', 'first_name', 'last_name')
    inlines = [OrderProductInline]


admin.site.register(Order, OrderAdmin)