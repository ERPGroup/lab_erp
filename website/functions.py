from django.shortcuts import render, redirect, get_object_or_404
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.db.models import Sum
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder

import pandas as pd
from datetime import datetime
from datetime import timedelta


from cart.cart import Cart
from django.core.paginator import Paginator
from random import randint

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
        # print(dict_category)
        del dict_category['_state']
        list_poduct_avaliable = Product_Category.objects.filter(archive=False,category_id_id=item).values_list('product_id_id')
        list_post = Post_Product.objects.exclude(pk__in=post_abort).filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-bought')[0:16]
        array_post = [] 
        for post in list_post:
            dict_post = post.__dict__
            del dict_post['_state']
            # if Product.objects.filter(pk=post.id).exists() == True:
            dict_product = Product.objects.get(pk=post.product_id_id).__dict__
            del dict_product['_state']
            image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
            dict_product['image'] = 'http://localhost:8000/product' + image.image_id.image_link.url
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
    input = Service_Ads_Post.objects.filter(state=2,purchase_service_id__is_active=True, purchase_service_id__state=4)
    result = []
    for item in input:
        if item.purchase_service_id.service_ads_id.position == "Slide":
            dict_result = dict()
            dict_result['position'] = item.purchase_service_id.service_ads_id.position
            dict_result['img_1'] = item.image_1
            dict_result['url_1'] = item.image_1_url
            dict_result['content_1'] = item.image_1_content
            dict_result['img_2'] = item.image_2
            dict_result['url_2'] = item.image_2_url
            dict_result['content_3'] = item.image_2_content
            dict_result['img_3'] = item.image_3
            dict_result['url_3'] = item.image_3_url
            dict_result['content_3'] = item.image_3_content
            result.append(dict_result)
        else:
            dict_result = dict()
            dict_result['position'] = item.purchase_service_id.service_ads_id.position
            dict_result['img_1'] = item.image_1
            dict_result['url_1'] = item.image_1_url
            dict_result['content_1'] = item.image_1_content
            result.append(dict_result)
    if result:
        return HttpResponse(json.dumps(result),content_type="application/json")   
    return HttpResponse(-1)
  

def get_data_collection(request, list_post):
    paginator = Paginator(list_post, 1)
    if 'page' in request.GET:
        page = request.GET.get('page')
    else:
        page = 1
    try:
        danhsach = paginator.page(page)
    except PageNotAnInteger:
        danhsach = paginator.page(1)
    except EmptyPage:
        danhsach = paginator.page(paginator.num_pages)
    array_post = []
    for item in danhsach:
        dict_post = item.__dict__
        del dict_post['_state']
        dict_product = Product.objects.get(pk=item.product_id_id).__dict__
        del dict_product['_state']
        image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
        dict_product['image'] = 'http://localhost:8000/product' + image.image_id.image_link.url
        dict_post['product'] = dict_product
        array_post.append(dict_post)
    return {
        'page': int(page),
        'has_next': danhsach.has_next(),
        'has_previous': danhsach.has_previous(),
        'length': list_post.count(),
        'data': array_post,
    }

def product_collection(request, id_category):
    if request.method == 'GET':
        if Category.objects.filter(pk=id_category).exists() == False:
            return HttpResponse('Category khong ton tai')
        category = Category.objects.get(pk = id_category)

        list_poduct_avaliable = Product_Category.objects.filter(archive=False, category_id_id=id_category).values_list('product_id_id')

        if 'newest' in request.GET:
            if request.GET.get('newest') == 'true':
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-created')
                data = get_data_collection(request, list_post)
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
            else: 
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('created')
                data = data = get_data_collection(request, list_post)
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

        if 'buiest' in request.GET:
            if request.GET.get('buiest') == 'true':
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-bought')
                data = get_data_collection(request, list_post)
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
            else: 
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('bought')
                data = get_data_collection(request, list_post)
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

        # if 'ratiest' in request.GET:
        #     if request.GET.get('ratiest') == 'true':
        #         list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-created')
        #         data = get_data_collection(request, list_post)
        #         return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
        #     else: 
        #         list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('created')
        #         data = get_data_collection(request, list_post)
        #         return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
        
        list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-created', '-bought')
        data = get_data_collection(request, list_post)
        data['name'] = category.name_category

        return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

def search(request):
    return



def product(request, id_product):
    if request.method == 'GET':
        ## can kiem tra xem co ton tai tin dang cho san pham nay khong?
        if Product.objects.filter(pk=id_product).exists() == False:
            return HttpResponse('Product khong ton tai')
        product = Product.objects.get(pk=id_product).__dict__
        del product['_state']
        account = Account.objects.get(pk=product['account_created_id']).__dict__
        del account['_state']
        product['merchant'] = account
        post = Post_Product.objects.get(is_lock=False, is_activity=True, product_id_id=id_product).__dict__
        del post['_state']
        product['post'] = post
        product_category = Product_Category.objects.filter(product_id=int(id_product), archive=False)
        list_category = []
        for item in product_category:
            category = Category.objects.get(pk=item.category_id_id).__dict__
            del category['_state']
            list_category.append(category)
        product['categories'] = list_category

        product_image = Product_Image.objects.filter(product_id=int(id_product), archive=False).order_by('image_id_id')
        list_image = []
        for item in product_image:
            image = Image.objects.get(pk=item.image_id_id).__dict__
            del image['_state']
            list_image.append(image)
        product['images'] = list_image

        link_types = Link_Type.objects.filter(parent_product=int(id_product), product_id__archive=False)

        list_version = []
        for item in link_types:
            vs = dict()
            attributes = []
            list_attr = Product_Attribute.objects.filter(product_id=item.product_id.id, archive=False).order_by('attribute_id')
            for x in list_attr:
                attr = Attribute.objects.get(pk=x.attribute_id_id).__dict__
                attr['value'] = x.value
                del attr['_state']
                attributes.append(attr)
            vs['attributes'] = attributes
            vs['price'] = item.product_id.price
            vs['name_product'] = item.product_id.name
            vs['id_product'] = item.product_id.id
            list_version.append(vs)
        product['version'] = list_version

        return HttpResponse(json.dumps(product, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
           
def post(request, id_post):
    if request.method == 'GET':
        if Post_Product.objects.filter(pk=id_post, is_lock=False, is_activity=True).exists() == False:
            return HttpResponse('Bai dang khong ton tai')

        post = Post_Product.objects.get(pk=id_post, is_lock=False, is_activity=True).__dict__
        del post['_state']
        product = Product.objects.get(pk=post['product_id_id']).__dict__
        del product['_state']
       

        product_category = Product_Category.objects.filter(product_id=product['id'], archive=False)
        list_category = []
        for item in product_category:
            category = Category.objects.get(pk=item.category_id_id).__dict__
            del category['_state']
            list_category.append(category)
        product['categories'] = list_category

        product_image = Product_Image.objects.filter(product_id=product['id'], archive=False).order_by('image_id_id')
        list_image = []
        for item in product_image:
            image = Image.objects.get(pk=item.image_id_id).__dict__
            del image['_state']
            list_image.append(image)
        product['images'] = list_image

        link_types = Link_Type.objects.filter(parent_product=product['id'], product_id__archive=False)

        list_version = []
        for item in link_types:
            vs = dict()
            attributes = []
            list_attr = Product_Attribute.objects.filter(product_id=item.product_id.id, archive=False).order_by('attribute_id')
            for x in list_attr:
                attr = Attribute.objects.get(pk=x.attribute_id_id).__dict__
                attr['value'] = x.value
                del attr['_state']
                attributes.append(attr)
            vs['attributes'] = attributes
            vs['price'] = item.product_id.price
            vs['name_product'] = item.product_id.name
            vs['id_product'] = item.product_id.id
            list_version.append(vs)
        product['version'] = list_version

        post['product'] = product
        account = Account.objects.get(pk=post['creator_id_id']).__dict__
        del account['_state']
        count_star = Rating.objects.aggregate(Sum('num_of_star'))
        count_person = Rating.objects.filter(merchant_id=account['id'], is_activity=True).count()
        if count_person == 0:
            account['rating'] = 0
        else:
            account['rating'] = float(count_star/count_person)
        post['merchant'] = account

        return HttpResponse(json.dumps(post, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
    

def get_data_hot_buy(request):
    if request.method == 'GET':
        list_post = Post_Product.objects.filter(is_lock=False, is_activity=True).order_by('-bought')[0:40]
        list_random = []
        while len(list_random) < 3:
            x = randint(0, list_post.count() - 1)
            if x not in list_random:
                list_random.append(x)
        posts = [list_post[list_random[0]], list_post[list_random[1]], list_post[list_random[2]]]
        print(posts)
        array_post = []
        for item in posts:
            dict_post = item.__dict__
            del dict_post['_state']
            dict_product = Product.objects.get(pk=item.product_id_id).__dict__
            del dict_product['_state']
            image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
            dict_product['image'] = 'http://localhost:8000/product' + image.image_id.image_link.url
            dict_post['product'] = dict_product
            array_post.append(dict_post)
        return HttpResponse(json.dumps({'datas': array_post}, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

def get_data_related(request, id_post):
    if request.method == 'GET':
        return
        
        