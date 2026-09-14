from django.contrib import admin
from .models import product

class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'category', 'is_available')
    
admin.site.register(product, productAdmin)
    
