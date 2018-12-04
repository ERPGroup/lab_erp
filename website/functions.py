from django.shortcuts import render, redirect, get_object_or_404
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder

import pandas as pd
from datetime import datetime
from datetime import timedelta


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


# function page index

def get_data(request):
    data = [] # du lieu tra ve json 
    post_abort = [] # du lieu bai dang tai khu vuc vip
    list_service = Service.objects.filter(visable_vip=True, is_active=True, archive=False).values_list('id')
    array_service = []
    for item in list_service:
        dict_service = Service.objects.get(pk=item[0]).__dict__
        del dict_service['_state']
        list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, post_type_id=item).order_by('-bought')[0:16]
        array_post = [] 
        for post in list_post:
            post_abort.append(post.id)
            dict_post = post.__dict__
            del dict_post['_state']
            # if Product.objects.filter(pk=post.id).exists() == True:
            dict_product = Product.objects.get(pk=post.product_id_id).__dict__
            del dict_product['_state']
            image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
            dict_product['image'] = 'http://localhost:8000/product' + image.image_id.image_link.url
            dict_post['product'] = dict_product
            array_post.append(dict_post)
        dict_service['posts'] = array_post
        array_service.append(dict_service)
    dict_data = {
        'type': 1,
        'data': array_service
    }
    data.append(dict_data)

    # danh sach san pham con lai theo danh muc san pham
    list_category = Category.objects.filter(is_active=True).values_list('id')
    array_category = []
    for item in list_category:
        dict_category = Category.objects.get(pk=item[0]).__dict__
        print(dict_category)
        del dict_category['_state']
        list_poduct_avaliable = Product_Category.objects.filter(archive=False,category_id_id=item).values_list('product_id_id')
        list_post = Post_Product.objects.exclude(product_id_id__in=post_abort).filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-bought')[0:16]
        array_post = [] 
        for post in list_post:
            dict_post = post.__dict__
            del dict_post['_state']
            # if Product.objects.filter(pk=post.id).exists() == True:
            dict_product = Product.objects.get(pk=post.product_id_id).__dict__
            del dict_product['_state']
            dict_post['product'] = dict_product
            array_post.append(dict_post)
        dict_category['posts'] = array_post
        array_category.append(dict_category)
    dict_data = {
        'type': 2,
        'data': array_category
    }
    data.append(dict_data)
    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json")   

@csrf_exempt
def getAds(request):
    key_search = request.POST['key']
    result = Service_Ads_Post.objects.filter(purchase_service_id__is_active=True, purchase_service_id__state=4, purchase_service_id__service_ads_id__position=key_search)
    if result:
        if key_search == "Slide":
            dict_result = dict()
            dict_result['img_1'] = result[0].image_1
            dict_result['url_1'] = result[0].image_1_url
            dict_result['content_1'] = result[0].image_1_content
            dict_result['img_2'] = result[0].image_2
            dict_result['url_2'] = result[0].image_2_url
            dict_result['content_3'] = result[0].image_2_content
            dict_result['img_3'] = result[0].image_3
            dict_result['url_3'] = result[0].image_3_url
            dict_result['content_3'] = result[0].image_3_content
            return HttpResponse(json.dumps(dict_result),content_type="application/json")   
        else:
            dict_result = dict()
            dict_result['img'] = result[0].image_1
            dict_result['url'] = result[0].image_1_url
            dict_result['content'] = result[0].image_1_content
            return HttpResponse(json.dumps(dict_result),content_type="application/json")       
    return HttpResponse(-1)
  

