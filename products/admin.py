from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """Admin model for Product to display relevant fields."""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image'
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """Admin model for Category to display relevant fields."""
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
