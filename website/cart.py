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
        return HttpResponse('Vui lòng lựa chọn phiên bản!')
    
    post = Post_Product.objects.filter(product_id_id=id_origin_product, is_lock=False, is_activity=True)

    if post.exists():
        availability = post[0].quantity - post[0].bought

        if product not in cart:
            cart.add(product, price=product.price)
            return HttpResponse(1)

        for x in cart.items:
            if x.product.id == product.id:
                if x.quantity + 1 > availability:
                    return HttpResponse('Sản phẩm không đủ số lượng!')
                else:
                    cart.add(product, price=product.price)
                    return HttpResponse(1)
    else:
        return HttpResponse('Sản phẩm không hợp lễ!')

def sub(request, id_product):
    cart = Cart(request.session)
    product = Product.objects.get(id=id_product)
    if product.type_product == False:
        id_origin_product = Link_Type.objects.get(product_id_id=id_product).parent_product
    else:
        return HttpResponse('Vui lòng lựa chọn phiên bản!')
    
    post = Post_Product.objects.filter(product_id_id=id_origin_product, is_lock=False, is_activity=True)
    if post.exists():
        if product not in cart:
            return HttpResponse("Sản phẩm không tồn tại trong giỏ hàng!")

        for x in cart.items:
            if x.product.id == product.id:
                qty = x.quantity - 1
                if qty <= 0:
                    cart.remove(product)
                    return HttpResponse(1)
                else:
                    cart.set_quantity(product, quantity=qty)
                    return HttpResponse(1)
    else:
        return HttpResponse('Sản phẩm không hợp lệ!')

def add_qty(request, id_product, qty):
    cart = Cart(request.session)
    product = Product.objects.get(id=id_product)
    if product.type_product == False:
        id_origin_product = Link_Type.objects.get(product_id_id=id_product).parent_product
    else:
        return HttpResponse(-2)
    
    post = Post_Product.objects.filter(product_id_id=id_origin_product, is_lock=False, is_activity=True)

    if post.exists():
        availability = post[0].quantity - post[0].bought

        if qty <= 0 or qty > availability:
            return HttpResponse(-1)
            
        if product not in cart:
            cart.add(product, quantity=qty, price=product.price)
            return HttpResponse("Thêm thành công")

        for x in cart.items:
            if x.product.id == product.id:
                if x.quantity + qty > availability:
                    return HttpResponse(-1)
                else:
                    cart.set_quantity(product, quantity=(x.quantity + qty))
                    return HttpResponse("Thêm thành công")
    else:
        return HttpResponse('Sản phẩm không hợp lễ!')

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
            return HttpResponse("Sản phẩm không tồn tại trong giỏ hàng!")
        if qty <= 0 or qty > availability:
            return HttpResponse('Số lượng không hợp lệ!') 
        
        cart.set_quantity(product, quantity=qty)
        return HttpResponse('Số lượng được thay đổi thành công!')    
    else:
        return HttpResponse('Sản phẩm không hợp lệ')


def remove(request, id_product):
    # kiem tra dang nhap
    #....................
    cart = Cart(request.session)
    product = Product.objects.get(pk=id_product)
    cart.remove(product)
    return HttpResponse("Đã xóa!")

def show(request):
    cart = Cart(request.session)
    for item in cart.items:
        print(item.quantity)
    return HttpResponse(cart.items)

def count(request):
    cart = Cart(request.session)
    return HttpResponse(cart.count)

def clear(request):
    cart = Cart(request.session)
    cart.clear()
    #messages.success(request, message='Danh sách sản phẩm đã được xóa!', extra_tags='alert')
    return HttpResponse("Da xoa")