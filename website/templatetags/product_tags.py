from django import template
import datetime
from website.models import *

register = template.Library()

@register.simple_tag(takes_context=True)
def get_image_product(context, id_product):
    product = Product.objects.get(id=id_product)
    if product.type_product == False:
        id_origin_product = Link_Type.objects.get(product_id_id=id_product).parent_product
    else:
        id_origin_product = id_product
    image = Product_Image.objects.filter(product_id_id=id_origin_product).order_by('image_id_id').first()
    return '/product/' + image.image_id.image_link.url

