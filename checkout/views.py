from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from checkout.forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SlvuwCToKLU8rrOujL3XkBcCd9jkdoa5uRx8Z70K8AyaPNcWIf6XqKChwzHNptWBIzE7lslbry6RkAZs0usVJ9P00zqcjQnpI',
        'client_secret': 'test_client',
    }

    return render(request, template, context)