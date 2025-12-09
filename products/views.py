from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """A view to show all products page."""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to show individual product details."""
    product = Product.objects.get(pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)