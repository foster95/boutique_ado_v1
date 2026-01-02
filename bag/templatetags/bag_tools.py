from django import template

register=template.Library()


@register.filter(names='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculate subtotal for an item in the bag."""
    return price * quantity

