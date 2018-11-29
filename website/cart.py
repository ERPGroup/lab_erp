from django.http import HttpResponse

from cart.cart import Cart
from website.models import *

import json

def add(request, id_product):
    # can kiem tra dang nhap
    #.........................
    
    cart = Cart(request.session)
    product = Product.objects.get(id=id_product)
    if product.type_product == False:
        id_origin_product = Link_Type.objects.get(product_id_id=id_product).parent_product
    else:
        return HttpResponse('Vui long lua chon phien ban')
    
    post = Post_Product.objects.filter(product_id_id=id_origin_product, is_lock=False, is_activity=True)
    if post.exists():
        availability = post[0].quantity - post[0].bought

        if product not in cart:
            cart.add(product, price=product.price)
            return HttpResponse("Them thanh cong")

        for x in cart.items:
            if x.product.id == product.id:
                if x.quantity + 1 > availability:
                    return HttpResponse('San pham khong du')
                else:
                    cart.add(product, price=product.price)
                    return HttpResponse("Them thanh cong")
    else:
        return HttpResponse('San pham khong hop le')

def sub(request, id_product):
    cart = Cart(request.session)
    product = Product.objects.get(id=id_product)
    if product.type_product == False:
        id_origin_product = Link_Type.objects.get(product_id_id=id_product).parent_product
    else:
        return HttpResponse('Vui long lua chon phien ban')
    
    post = Post_Product.objects.filter(product_id_id=id_origin_product, is_lock=False, is_activity=True)
    if post.exists():
        if product not in cart:
            return HttpResponse("San pham khong ton tai trong gio hang")

        for x in cart.items:
            if x.product.id == product.id:
                qty = x.quantity - 1
                if qty <= 0:
                    cart.remove(product)
                    return HttpResponse("Da giam 1 san pham thanh cong")
                else:
                    cart.set_quantity(product, quantity=qty)
                    return HttpResponse("Da giam 1 san pham thanh cong")
    else:
        return HttpResponse('San pham khong hop le')

def set_qty(request, id_product, qty):
    cart = Cart(request.session)
    product = Product.objects.get(id=id_product)
    if product.type_product == False:
        id_origin_product = Link_Type.objects.get(product_id_id=id_product).parent_product
    else:
        id_origin_product = id_product
    
    post = Post_Product.objects.filter(product_id_id=id_origin_product, is_lock=False, is_activity=True)
    if post.exists():
        availability = post[0].quantity - post[0].bought
        if product not in cart:
            return HttpResponse("San pham khong ton tai trong gio hang")
        if qty <= 0 or qty > availability:
            return HttpResponse('So luong khong hop le') 
        
        cart.set_quantity(product, quantity=qty)
        return HttpResponse('So luong duoc thay doi thanh cong')
                
    else:
        return HttpResponse('San pham khong hop le')


def remove(request, id_product):
    # kiem tra dang nhap
    #....................
    cart = Cart(request.session)
    product = Product.objects.get(pk=id_product)
    cart.remove(product)
    return HttpResponse("Da xoa")

def show(request):
    cart = Cart(request.session)
    return HttpResponse(cart.items)

def clear(request):
    cart = Cart(request.session)
    cart.clear()
    #messages.success(request, message='Danh sách sản phẩm đã được xóa!', extra_tags='alert')
    return HttpResponse("Da xoa")