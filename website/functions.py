from django.shortcuts import render, redirect, get_object_or_404
from admin import views
import random
from  passlib.hash import pbkdf2_sha256
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
from sender import Mail, Message


from cart.cart import Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import randint

def get_avatar_product(request, id_product):
    ''' Lấy ra hình ảnh đại diện cho sản phẩm'''
    if request.method == 'GET':
        image = Product_Image.objects.filter(product_id_id=id_product).order_by('image_id_id').first()
        return HttpResponse(image.image_id.image_link.url)

def product_by_category(request, id_category):
    ''' '''
    if request.method == 'GET':
        if Category.objects.filter(pk=id_category).exists() == False:
            return HttpResponse('Không tìm thấy danh mục bạn chọn')
        else:
            list_pro_cat = Product_Category.objects.filter(category_id_id=id_category).values_list('product_id_id')
            list_product = Post_Product.objects.filter(product_id_id__in=list_pro_cat, is_lock=False, is_activity=True)
            x = serialize('json', [list_product[0].product_id])
            c = (list_product)
            return HttpResponse(x, content_type="application/json")
            # x = serialize('json', list_product[0].product_id)
            # print(type(list_product[0].product_id))
            # return HttpResponse(serialize('json', list_product))

def categorys(request):
    if request.method  == 'GET':
        return HttpResponse(serialize('json', Category.objects.all()), content_type="application/json")

@csrf_exempt       
def payment(request):
    ''' Tạo đơn hàng '''
    # check user  dang nhap vao he thong chua?
    # cap nhat lai so luong cua bai viet

    if request.method == 'POST':
        if 'user' not in request.session:
            return HttpResponse('Vui lòng đăng nhập để thanh toán')
        cart = Cart(request.session)

        if cart.count == 0:
            return HttpResponse('Bạn chưa có sản phẩm nào trong giỏ hàng')

        name  = request.POST.get('inputName')
        phone = request.POST.get('inputPhone')
        address = request.POST.get('inputAddress')
        note = request.POST.get('inputNote')
        
        customer = Account.objects.get(pk = request.session.get('user')['id'])

        try:
            order = Order(
                name=name,
                customer=customer,
                amount=cart.total,
                email=customer.email,
                address=address,
                phone=phone,
                note=note,
                state=2,
                is_paid=False,
                is_activity=True,
                archive=False,
            )
            order.save()

            for item in cart.items:
                product_origin = Link_Type.objects.get(product_id_id=item.product.id)
                post = Post_Product.objects.filter(product_id_id=product_origin.parent_product, is_lock=False, is_activity=True)
                order_detail = Order_Detail(
                    order=order,
                    product=item.product,
                    post=post[0],
                    merchant=item.product.account_created,
                    quantity=item.quantity,
                    price= item.price,
                    discount=item.product.discount_percent,
                    state=2,
                    confirm_of_merchant=False
                )
                order_detail.save()
                product_orgin = Link_Type.objects.get(product_id_id=item.product.id).parent_product
                post = Post_Product.objects.filter(product_id_id=product_orgin).order_by('-id').first()
                bought = post.bought
                post.bought = bought + item.quantity
                if (item.quantity + bought) >= post.quantity:
                    post.is_lock = True
                post.save()
        except:
            raise
        cart.clear()
        send_email_notifile(customer.email, 'Sản phẩm đặt mua thành công', 'Bạn có thể xem thông tin đơn hàng tại <a href="http://13.67.105.209:8000/customer/bill_detail/'+ str(order.id) +'"> đây</a>')
        return HttpResponse(1)

    return HttpResponse('Lỗi hệ thống!')


# function page index

# def check_expire_post(id_post):
#     post = Post_Product.objects.get(pk=id_post)
#     if post.expire.replace(tzinfo=None) <= datetime.now():
#         return 1
#     return 0
    
def get_data(request):
    data = [] # du lieu tra ve json 
    post_abort = [] # du lieu bai dang tai khu vuc vip
    list_service = Service.objects.filter(visable_vip=True, is_active=True, archive=False).order_by('-amount').values_list('id')
    array_service = []
    for item in list_service:
        dict_service = Service.objects.get(pk=item[0]).__dict__
        del dict_service['_state']
        list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, post_type_id=item, creator_id__is_lock=False).order_by('-bought')
        array_post = [] 
        index = 0
        for post in list_post:
            if index == 16:
                break
            if post.expire.replace(tzinfo=None) > datetime.now():
                post_abort.append(post.id)
                dict_post = post.__dict__
                count_star = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
                if count_star == None:
                    count_star = 0
                count_person = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
                if count_person == 0:
                    dict_post['rating'] = float(0)
                else:
                    dict_post['rating'] = float(round(count_star/count_person, 1))
                
                del dict_post['_state']
                # if Product.objects.filter(pk=post.id).exists() == True:
                dict_product = Product.objects.get(pk=post.product_id_id).__dict__
                del dict_product['_state']
                list_price = Link_Type.objects.filter(parent_product=dict_product['id'], product_id__archive=False).values_list('product_id__price')
                dict_product['range_price'] = [max(list_price)[0], min(list_price)[0]]
                image = Product_Image.objects.filter(product_id_id=dict_product['id'], archive=False).order_by('image_id_id').first()
                dict_product['image'] = 'http://13.67.105.209:8000/product' + image.image_id.image_link.url
                dict_post['product'] = dict_product
                array_post.append(dict_post)
                index = index + 1
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
        list_post = Post_Product.objects.exclude(pk__in=post_abort).filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, creator_id__is_lock=False).order_by('-bought')[0:16]
        array_post = [] 
        for post in list_post:
            if post.expire.replace(tzinfo=None) > datetime.now():
                dict_post = post.__dict__

                count_star = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
                if count_star == None:
                    count_star = 0
                count_person = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
                if count_person == 0:
                    dict_post['rating'] = float(0)
                else:
                    dict_post['rating'] = float(round(count_star/count_person, 1))

                del dict_post['_state']
                # if Product.objects.filter(pk=post.id).exists() == True:
                dict_product = Product.objects.get(pk=post.product_id_id).__dict__
                list_price = Link_Type.objects.filter(parent_product=dict_product['id'], product_id__archive=False).values_list('product_id__price')
                dict_product['range_price'] = [max(list_price)[0], min(list_price)[0]]
                del dict_product['_state']
                image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
                dict_product['image'] = 'http://13.67.105.209:8000/product' + image.image_id.image_link.url
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
    paginator = Paginator(list_post, 12)
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
        if item.expire.replace(tzinfo=None) > datetime.now() and item.post_type.visable_vip == True:
            dict_post['vip'] = True
        else:
            dict_post['vip'] = False
        count_star = Rating.objects.filter(merchant_id=item.creator_id.id).aggregate(Sum('num_of_star'))['num_of_star__sum']
        if count_star == None:
            count_star = 0
        count_person = Rating.objects.filter(merchant_id=item.creator_id.id, is_activity=True).count()
        if count_person == 0:
            dict_post['rating'] = float(0)
        else:
            dict_post['rating'] = float(round(count_star/count_person, 1))
        del dict_post['_state']
        dict_product = Product.objects.get(pk=item.product_id_id).__dict__
        del dict_product['_state']
        list_price = Link_Type.objects.filter(parent_product=dict_product['id'], product_id__archive=False).values_list('product_id__price')
        dict_product['range_price'] = [max(list_price)[0], min(list_price)[0]]
        image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
        dict_product['image'] = 'http://13.67.105.209:8000/product' + image.image_id.image_link.url
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
            return HttpResponse('Danh mục không tồn tại!')
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
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

        if 'pricest' in request.GET:
            if request.GET.get('pricest') == 'true':
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-product_id__price')
                data = get_data_collection(request, list_post)
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
            else: 
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('product_id__price')
                data = get_data_collection(request, list_post)
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

        if 'filter' in request.GET:
            if request.GET.get('filter') == 'true':
                if 'min' in request.GET:
                    min_price = int(request.GET.get('min'))
                else:
                    min_price = 0

                if 'max' in request.GET:
                    max_price = int(request.GET.get('max'))
                else:
                    max_price = 0
                # print(list_poduct_avaliable)
                list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__price__gte=min_price, product_id__price__lte=max_price).order_by('product_id__price')
                data = get_data_collection(request, list_post)
                data['name'] = category.name_category
                return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
        
        list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-created', '-bought')
        data = get_data_collection(request, list_post)
        data['name'] = category.name_category

        return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

def search(request):
    if request.method == 'GET':
        if 'r' in request.GET:
            keyword = request.GET.get('r')

            list_poduct_avaliable = Product_Category.objects.filter(archive=False).values_list('product_id_id')

            if 'newest' in request.GET:
                if request.GET.get('newest') == 'true':
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('-created')
                    data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
                else: 
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('created')
                    data = data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

            if 'buiest' in request.GET:
                if request.GET.get('buiest') == 'true':
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('-bought')
                    data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
                else: 
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('bought')
                    data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

            if 'pricest' in request.GET:
                if request.GET.get('pricest') == 'true':
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('-product_id__price')
                    data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
                else: 
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('product_id__price')
                    data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

            if 'filter' in request.GET:
                if request.GET.get('filter') == 'true':
                    if 'min' in request.GET:
                        min_price = int(request.GET.get('min'))
                    else:
                        min_price = 0

                    if 'max' in request.GET:
                        max_price = int(request.GET.get('max'))
                    else:
                        max_price = 0
                    # print(list_poduct_avaliable)
                    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__price__gte=min_price, product_id__name__icontains=keyword, product_id__price__lte=max_price).order_by('product_id__price')
                    data = get_data_collection(request, list_post)
                    data['name'] = keyword
                    return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )


            list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable, product_id__name__icontains=keyword).order_by('-created', '-bought')
            data = get_data_collection(request, list_post)
            data['name'] = keyword

            return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
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
            return HttpResponse('Bài đăng không tồn tại')

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
        count_star = Rating.objects.filter(merchant_id=account['id']).aggregate(Sum('num_of_star'))['num_of_star__sum']
        if count_star == None:
            count_star = 0
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
        print(list_post)
        list_random = []
        count = list_post.count()
        while len(list_random) < 3:
            x = randint(0, count - 1)
            if x not in list_random:
                list_random.append(x)
            if len(list_random) == count:
                break
        print(list_random)
        if list_post.count() < 4:
            posts = list_post
        else:
            posts = [list_post[list_random[0]], list_post[list_random[1]], list_post[list_random[2]]]
        print(posts)
        array_post = []
        for post in posts:
            dict_post = post.__dict__

            count_star = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
            if count_star == None:
                count_star = 0
            count_person = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
            if count_person == 0:
                dict_post['rating'] = float(0)
            else:
                dict_post['rating'] = float(round(count_star/count_person, 1))

            del dict_post['_state']
            # if Product.objects.filter(pk=post.id).exists() == True:
            dict_product = Product.objects.get(pk=post.product_id_id).__dict__
            list_price = Link_Type.objects.filter(parent_product=dict_product['id'], product_id__archive=False).values_list('product_id__price')
            dict_product['range_price'] = [max(list_price)[0], min(list_price)[0]]
            del dict_product['_state']
            image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
            dict_product['image'] = 'http://13.67.105.209:8000/product' + image.image_id.image_link.url
            dict_post['product'] = dict_product
            array_post.append(dict_post)
        return HttpResponse(json.dumps({'datas': array_post}, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )

def get_data_related(request, id_category):
    if request.method == 'GET':
        if Category.objects.filter(pk=id_category).exists() == False:
            return HttpResponse('Danh mục không tồn tại!')

        category = Category.objects.get(pk = id_category)
        list_poduct_avaliable = Product_Category.objects.filter(archive=False, category_id_id=id_category).values_list('product_id_id')
        list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-bought')[0:40]
        list_random = []
        while len(list_random) >= 4:
            x = randint(0, list_post.count() - 1)
            if x not in list_random:
                list_random.append(x)
        if list_post.count() < 5:
            posts = list_post
        else:
            posts = [list_post[list_random[0]], list_post[list_random[1]], list_post[list_random[2]], list_post[list_random[3]]]
        # print(posts)
        array_post = []
        for post in posts:
            dict_post = post.__dict__
            count_star = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
            if count_star == None:
                count_star = 0
            count_person = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
            if count_person == 0:
                dict_post['rating'] = float(0)
            else:
                dict_post['rating'] = float(round(count_star/count_person, 1))

            del dict_post['_state']
            # if Product.objects.filter(pk=post.id).exists() == True:
            dict_product = Product.objects.get(pk=post.product_id_id).__dict__
            list_price = Link_Type.objects.filter(parent_product=dict_product['id'], product_id__archive=False).values_list('product_id__price')
            dict_product['range_price'] = [max(list_price)[0], min(list_price)[0]]
            del dict_product['_state']
            image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
            dict_product['image'] = 'http://13.67.105.209:8000/product' + image.image_id.image_link.url
            dict_post['product'] = dict_product
            array_post.append(dict_post)
        return HttpResponse(json.dumps({'datas': array_post}, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )


def get_profile_payment(request):
    if request.method == 'GET':
        if 'user' not in request.session:
            return HttpResponse(-1)
        user = Account.objects.get(pk = request.session.get('user')['id'])
        data = dict()
        data['name']  = user.name
        data['phone'] = user.phone
        data['address'] = user.address

        return HttpResponse(json.dumps(data), content_type="application/json")

def random_code_activity(length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

@csrf_exempt
def register(request):
    if request.method  == 'POST':
        username = request.POST.get('inputUsername')
        if Account.objects.filter(username=username).exists() == True:
            return HttpResponse('Username đã tồn tại!')
        email = request.POST.get('inputEmail')
        if Account.objects.filter(email=email).exists() == True:
            return HttpResponse('Email đã tồn tại!')
        password = request.POST.get('inputPassword')
        name = request.POST.get('inputFullname')
        birthday = request.POST.get('inputBirthday')
        sex = request.POST.get('inputSex')
        
        option_acc = request.POST.get('inputOptionAcc')
        if int(option_acc) == 0:
            code = random_code_activity(40)
            new_account = Account(
                username = username,
                email=email,
                password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
                name=name,
                birthday = birthday,
                sex=sex,
                code_act_account=code,
            )
            new_account.save()
            link = 'activity/%s/%s/' % (email, code)
            action = 'Vui lòng bấm nút bên dưới để kích hoạt'
            template = template_register(name, action, link)
            header = 'Xác thực tài khoản'
            send_email_notifile(email, header, template)

        elif int(option_acc) == 1:
            cmnd = request.POST.get('inputID')
            phone = request.POST.get('inputTel')
            address = request.POST.get('inputAddress')
            store = request.POST.get('inputStore')
            code_act_merchant = random_code_activity(40)
            new_account = Account(
                username = username,
                email = email,
                password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
                name=name,
                code_act_merchant=code_act_merchant,
                activity_account=False,
                id_card=cmnd,
                phone=phone,
                address=address,    
                name_shop=store,
            )
            new_account.save()
            # Them Gift khi merchant duoc tao
            new_gift = Account_Gift(
                account = Account.objects.get(username=username)
            )
            new_gift.save()
            # end gift
            link = 'activity_merchant/%s/%s/' % (email, code_act_merchant)
            action = 'Vui lòng bấm nút bên dưới để kích hoạt'
            template = template_register(name, action, link)
            header = 'Xác thực tài khoản'
            send_email_notifile(email, header, template)
            # send_mail_register('activity_merchant', email, code_act_merchant)
        elif int(option_acc) == 2:
            cmnd = request.POST.get('inputID')
            phone = request.POST.get('inputTel')
            address = request.POST.get('inputAddress')
            store = request.POST.get('inputStore')
            code_act_ads = random_code_activity(40)
            new_account = Account(
                username = username,
                email = email,
                password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
                name=name,
                code_act_ads=code_act_ads,
                activity_account=False,
                id_card=cmnd,
                phone=phone,
                address=address,    
                name_shop=store,
            )
            new_account.save()
            link = 'activity_ad/%s/%s/' % (email, code_act_ads)
            action = 'Vui lòng bấm nút bên dưới để kích hoạt'
            template = template_register(name, action, link)
            header = 'Xác thực tài khoản'
            send_email_notifile(email, header, template)
        return HttpResponse(1)

@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        if Account.objects.filter(email=email).exists() == False:
            return HttpResponse('Lỗi! Tài khoản không tồn tại!')
        account = Account.objects.get(email=email)
        if account.activity_account == False:
            return HttpResponse('Lỗi! Tài khoản chưa được kích hoạt!')
        if account.is_lock == True:
            return HttpResponse('Lỗi! Tài khoản đã bị khóa!')
        code_act_account = random_code_activity(40)
        account.code_act_account = code_act_account
        account.save()
        link = 'request_new_password/%s/%s/' % (email, code_act_account)
        action = 'Vui lòng bấm nút bên dưới để đổi mật khẩu'
        template = template_register(account.name, action, link)
        header = 'Lấy lại mật khẩu'
        send_email_notifile(email, header, template)
        return HttpResponse(1)
    return HttpResponse(503)

def get_product_shop(request, id_shop):
    if request.method == 'GET':
        if Account.objects.filter(pk=id_shop, activity_merchant=True, is_lock=False).exists() == False:
            return HttpResponse('Lỗi! Shop không tồn tại')
        account = Account.objects.filter(pk=id_shop, activity_merchant=True, is_lock=False).first()
        posts = Post_Product.objects.filter(creator_id_id=account.id, is_lock=False, is_activity=True)
        data = get_data_collection(request, posts)
        data['name'] = account.name_shop
        return HttpResponse(json.dumps(data, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json" )
    return HttpResponse(503)

@csrf_exempt
def rating_merchant_shop(request, id_shop):
    if request.method == 'POST':
        if 'user' not in request.session:
            return HttpResponse('Vui lòng đăng nhập để đánh giá')
        if Account.objects.filter(pk=id_shop, activity_merchant=True, is_lock=False).exists() == False:
            return HttpResponse('Lỗi! Shop không tồn tại')
        account = Account.objects.filter(pk=id_shop, activity_merchant=True, is_lock=False).first()
        if Rating.objects.filter(customer_id=request.session.get('user')['id'], merchant_id=account.id).exists() == True:
            return HttpResponse('Lỗi! Bạn đã đánh giá trước đó!')
        num_star = request.POST.get('num_star')
        comment = request.POST.get('comment')
        customer_id = request.session.get('user')['id']
        list_order = Order.objects.filter(customer_id=customer_id).values_list('id')
        if Order_Detail.objects.filter(merchant_id=account.id, state=1, order_id__in=list_order).exists() == False:
            return HttpResponse('Bạn chưa mua sản phẩm của người bán!')

        Rating.objects.create(
            merchant=account,
            customer=Account.objects.get(pk=customer_id),
            num_of_star=num_star,
            comment=comment,
            confirm_bought=True,
            is_activity=True,
        )

        header = 'Bạn được người mua "'+ Account.objects.get(pk=customer_id).name +'" đánh giá!'
        body = '<h1>Bạn được đánh giá '+ num_star +' sao!</h1>'
        send_email_notifile(account.id.email, header, body)

        rating_count = Rating.objects.filter(merchant_id=account.id, is_activity=True).count()
        if rating_count == 0:
            header = 'Cảnh cáo!'
            body = '<h1>Tài khoản của bạn có nguy cơ bị khóa!\n Vui lòng liên hệ với chúng tôi để biết thêm thông tin!</h1>'
            send_email_notifile(account.id.email, header, body)
        rating_point = Rating.objects.filter(merchant_id=account.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
        if rating_point == None:
            rating_point = 0
        if (float(rating_point/rating_count) < 2):
            header = 'Cảnh cáo!'
            body = '<h1>Tài khoản của bạn có nguy cơ bị khóa!\n Vui lòng liên hệ với chúng tôi để biết thêm thông tin!</h1>'
            send_email_notifile(account.id.email, header, body)
        
        return HttpResponse(1)

@csrf_exempt
def rating_merchant(request, id_post):
    if request.method == 'POST':
        if 'user' not in request.session:
            return HttpResponse('Vui lòng đăng nhập để đánh giá')
        if Post_Product.objects.filter(pk=id_post, is_lock=False, is_activity=True).exists() == False:
            return HttpResponse('Lỗi! Tin đăng không tồn tại')
        post = Post_Product.objects.filter(pk=id_post, is_lock=False, is_activity=True).first()
        if Rating.objects.filter(customer_id=request.session.get('user')['id'], merchant_id=post.creator_id.id).exists() == True:
            return HttpResponse('Lỗi! Bạn đã đánh giá trước đó!')
        num_star = request.POST.get('num_star')
        comment = request.POST.get('comment')
        customer_id = request.session.get('user')['id']
        list_order = Order.objects.filter(customer_id=customer_id).values_list('id')
        if Order_Detail.objects.filter(merchant_id=post.creator_id.id, state=1, order_id__in=list_order).exists() == False:
            return HttpResponse('Bạn chưa mua sản phẩm của người bán!')

        Rating.objects.create(
            merchant=post.creator_id,
            customer=Account.objects.get(pk=customer_id),
            num_of_star=num_star,
            comment=comment,
            confirm_bought=True,
            is_activity=True,
        )

        header = 'Bạn được người mua "'+ Account.objects.get(pk=customer_id).name +'" đánh giá!'
        body = '<h1>Bạn được đánh giá '+ num_star +' sao!</h1>'
        send_email_notifile(post.creator_id.email, header, body)

        rating_count = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
        if rating_count == 0:
            header = 'Cảnh cáo!'
            body = '<h1>Tài khoản của bạn có nguy cơ bị khóa!\n Vui lòng liên hệ với chúng tôi để biết thêm thông tin!</h1>'
            send_email_notifile(post.creator_id.email, header, body)
        rating_point = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
        if rating_point == None:
            rating_point = 0
        if (float(rating_point/rating_count) < 2):
            header = 'Cảnh cáo!'
            body = '<h1>Tài khoản của bạn có nguy cơ bị khóa!\n Vui lòng liên hệ với chúng tôi để biết thêm thông tin!</h1>'
            send_email_notifile(post.creator_id.email, header, body)
        
        return HttpResponse(1)


def send_email_notifile(email, body, content):

    mail = Mail(
        'smtp.gmail.com', 
        port='465', 
        username='dinhtai018@gmail.com', 
        password='wcyfglkfcshkxoaa',
        use_ssl=True,
        use_tls=False,
        debug_level=False
    )
    msg = Message(body)
    msg.fromaddr = ("Website C2C", "dinhtai018@gmail.com")
    msg.to = email
    msg.body = body
    msg.html = content
    msg.reply_to = 'no-reply@gmail.com'
    msg.charset = 'utf-8'
    msg.extra_headers = {}
    msg.mail_options = []
    msg.rcpt_options = []
    mail.send(msg)



def template_register(name, action, link):
    template_email = """
    <!DOCTYPE html>
    <html>
    <head>
    <title></title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <style type="text/css">
        /* CLIENT-SPECIFIC STYLES */
        body, table, td, a{-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;} /* Prevent WebKit and Windows mobile changing default text sizes */
        table, td{mso-table-lspace: 0pt; mso-table-rspace: 0pt;} /* Remove spacing between tables in Outlook 2007 and up */
        img{-ms-interpolation-mode: bicubic;} /* Allow smoother rendering of resized image in Internet Explorer */

        /* RESET STYLES */
        img{border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none;}
        table{border-collapse: collapse !important;}
        body{height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important;}

        /* iOS BLUE LINKS */
        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: none !important;
            font-size: inherit !important;
            font-family: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important;
        }

        /* MOBILE STYLES */
        @media screen and (max-width: 525px) {

            /* ALLOWS FOR FLUID TABLES */
            .wrapper {
            width: 100% !important;
                max-width: 100% !important;
            }

            /* ADJUSTS LAYOUT OF LOGO IMAGE */
            .logo img {
            margin: 0 auto !important;
            }

            /* USE THESE CLASSES TO HIDE CONTENT ON MOBILE */
            .mobile-hide {
            display: none !important;
            }

            .img-max {
            max-width: 100% !important;
            width: 100% !important;
            height: auto !important;
            }

            /* FULL-WIDTH TABLES */
            .responsive-table {
            width: 100% !important;
            }

            /* UTILITY CLASSES FOR ADJUSTING PADDING ON MOBILE */
            .padding {
            padding: 10px 5% 15px 5% !important;
            }

            .padding-meta {
            padding: 30px 5% 0px 5% !important;
            text-align: center;
            }

            .padding-copy {
                padding: 10px 5% 10px 5% !important;
            text-align: center;
            }

            .no-padding {
            padding: 0 !important;
            }

            .section-padding {
            padding: 50px 15px 50px 15px !important;
            }

            /* ADJUST BUTTONS ON MOBILE */
            .mobile-button-container {
                margin: 0 auto;
                width: 100% !important;
            }

            .mobile-button {
                padding: 15px !important;
                border: 0 !important;
                font-size: 16px !important;
                display: block !important;
            }

        }

        /* ANDROID CENTER FIX */
        div[style*="margin: 16px 0;"] { margin: 0 !important; }
    </style>
    </head>
    """
    
    template_email += """
    <body style="margin: 0 !important; padding: 0 !important;">

    <!-- HIDDEN PREHEADER TEXT -->
    <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
        Entice the open with some amazing preheader text. Use a little mystery and get those subscribers to read through...
    </div>

    <!-- HEADER -->
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td bgcolor="#ffffff" align="center">
                <!--[if (gte mso 9)|(IE)]>
                <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
                <tr>
                <td align="center" valign="top" width="500">
                <![endif]-->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 500px;" class="wrapper">
                    <tr>
                        <td align="center" valign="top" style="padding: 15px 0;" class="logo">
                            <a href="http://13.67.105.209:8000" target="_blank">
                                <span style="font-size:38px; display: block; font-family: Helvetica, Arial, sans-serif; color: red;" border="0">Tablet Plaza</span>
                            </a>
                        </td>
                    </tr>
                </table>
                <!--[if (gte mso 9)|(IE)]>
                </td>
                </tr>
                </table>
                <![endif]-->
            </td>
        </tr>
        <tr>
            <td bgcolor="#D8F1FF" align="center" style="padding: 70px 15px 70px 15px;" class="section-padding">
                <!--[if (gte mso 9)|(IE)]>
                <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
                <tr>
                <td align="center" valign="top" width="500">
                <![endif]-->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 500px;" class="responsive-table">
                    <tr>
                        <td>
                            <!-- HERO IMAGE -->
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td>
                                        <!-- COPY -->
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="center" style="font-size: 25px; font-family: Helvetica, Arial, sans-serif; color: #333333; padding-top: 30px;" class="padding">Xin chào, {}</td>
                                            </tr>
                                            <tr>
                                                <td align="center" style="font-size: 25px; font-family: Helvetica, Arial, sans-serif; color: #333333; padding-top: 30px;" class="padding">Đăng ký tài khoản thành công</td>
                                            </tr>
                                            <tr>
                                                <td align="center" style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; font-family: Helvetica, Arial, sans-serif; color: #666666;" class="padding">{}</td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <!-- BULLETPROOF BUTTON -->
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="center" style="padding-top: 25px;" class="padding">
                                                    <table border="0" cellspacing="0" cellpadding="0" class="mobile-button-container">
                                                        <tr>
                                                            <td align="center" style="border-radius: 3px;" bgcolor="#256F9C"><a href="http://13.67.105.209:8000/{}" target="_blank" style="font-size: 16px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; border-radius: 3px; padding: 15px 25px; border: 1px solid #256F9C; display: inline-block;" class="mobile-button">Kích hoạt &rarr;</a></td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                <!--[if (gte mso 9)|(IE)]>
                </td>
                </tr>
                </table>
                <![endif]-->
            </td>
        </tr>
        <tr>
            <td bgcolor="#ffffff" align="center" style="padding: 20px 0px;">
                <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" style="max-width: 500px;" class="responsive-table">
                    <tr>
                        <td align="center" style="font-size: 12px; line-height: 18px; font-family: Helvetica, Arial, sans-serif; color:#666666;">
                            56 Nguyễn Trải, Phường 3, Quận 5, Tp. HCM
                            <br>
                            <a href="http://13.67.105.209:8000" target="_blank" style="color: #666666; text-decoration: none;">Trang chủ</a>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>

    </body>
    </html>
    """.format(name, action , link)
    return template_email