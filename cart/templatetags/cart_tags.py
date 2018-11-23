from django import template
import datetime
from cart.cart import Cart
from cart.settings import CART_TEMPLATE_TAG_NAME


register = template.Library()

@register.simple_tag(takes_context=True, name=CART_TEMPLATE_TAG_NAME)
def get_cart(context, session_key=None):
    """
    Make the cart object available in template.

    Sample usage::

        {% load carton_tags %}
        {% get_cart as cart %}
        {% for product in cart.products %}
            {{ product }}
        {% endfor %}
    """
    request = context['request']
    return Cart(request.session, session_key=session_key)

#register.simple_tag(takes_context=True, name=CART_TEMPLATE_TAG_NAME)
