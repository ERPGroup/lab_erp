from django.shortcuts import render, redirect, get_object_or_404
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, timedelta
import json

from cart.cart import Cart

def get_avatar_product(request, id_product):
    if request.method == 'GET':
        image = Product_Image.objects.filter(product_id_id=id_product).order_by('image_id_id').first()
        return HttpResponse(image.image_id.image_link.url)

def product_by_category(request, id_category):
    if request.method == 'GET':
        # start = 0
        # end = 0
        # num = 12
        # if 'page' not in request.GET or int(request.GET.get('page')) < 1:
        #     start = 0
        #     end = 11
        # else:
        #     start = int(request.GET.get('page'))* 12
        #     end = start + 12

        if Category.objects.filter(pk=id_category).exists() == False:
            return HttpResponse('Not found this category')
        else:
            list_pro_cat = Product_Category.objects.filter(category_id_id=id_category).values_list('product_id_id')
            list_product = Post_Product.objects.filter(product_id_id__in=list_pro_cat, is_lock=False, is_activity=True)
            x = serialize('json', [list_product[0].product_id])
            c = (list_product)
            print((get_object_or_404(c)))
            return HttpResponse(x, content_type="application/json")
            # x = serialize('json', list_product[0].product_id)
            # print(type(list_product[0].product_id))
            # return HttpResponse(serialize('json', list_product))

@csrf_exempt       
def payment(request):
    # check user  dang nhap vao he thong chua?

    if request.method == 'POST':
        cart = Cart(request.session)


        email = request.POST.get('inputEmail')
        name  = request.POST.get('inputName')
        phone = request.POST.get('inputPhone')
        address = request.POST.get('inputAddress')
        note = request.POST.get('inputNote')
        
        customer = Account.objects.get(pk = request.session.get('user')['id'])

        order = Order(
            customer=customer,
            amount=cart.total,
            email=email,
            address=address,
            phone=phone,
            state=2,
            is_paid=False,
            is_activity=True,
            archive=False,
        )
        order.save()

        for item in cart.items:
            order_detail = Order_Detail(
                order=order,
                product=item.product,
                merchant=item.product.account_created,
                quantity=item.quantity,
                price= item.product.price,
                state=2,
                confirm_of_merchant=False
            )
            order_detail.save()
        return HttpResponse('Thanh Cong!')

    return HttpResponse('error')