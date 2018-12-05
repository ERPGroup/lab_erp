from django.shortcuts import render, redirect
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import re
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta

def check_rule(request):
    # if 'user' in request.session:
    #     user = request.session.get('user')
    #     print(user['role'])
    #     if 0 in user['role']:
    #         print(user)
    #         return 1
    #     return 0
    # return 0
    return 1

# Phuc doc tham khao Service

def services(request):
    if request.method == 'GET':
        if request.GET.get('table') == 'true':
            services = []
            service_all = Service.objects.all()
            for item in service_all:
                service = []
                service.append('<a href="/admin/service/edit/'+ str(item.id) +'">'+ str(item.service_name) +'</a>')
                service.append(str(item.value) + ' tin')
                service.append(str(item.day_limit)+ ' ngày')
                service.append(str(item.amount)+ ' VNĐ')
                if item.is_active == True:
                    service.append('<b style="color:green">Đang bán</b>')
                else:
                    service.append('<b style="color:red">Ngưng bán</b>')
                services.append(service)
            return HttpResponse(json.dumps(services), content_type="application/json")
        return HttpResponse(serialize('json', Service.objects.all()), content_type="application/json")
    return HttpResponse('error')

# Service_add
@csrf_exempt    
def service_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        print(request.POST)
        service_name = request.POST.get('inputServiceName')
        amount = request.POST.get('inputAmount')
        value = request.POST.get('inputValue')
        quantity_product = request.POST.get('inputQuantityProduct')
        day_limit = request.POST.get('inputDayLimit')
        visable_vip = request.POST.get('inputVisableVip')
        is_active = request.POST.get('inputIsActive')

        #try:
        service = Service(
            service_name=service_name,
            amount=amount,
            value=value,
            quantity_product=quantity_product,
            day_limit=day_limit,
            visable_vip=visable_vip,
            is_active=is_active,
            creator_id=request.session.get('user')['id'],
        )
        service.save()
        accounts = Account.objects.filter(activity_merchant=True)
        for item in accounts:
            Account_Service.objects.create(
                account = item,
                service = service,
            )
        return HttpResponse(1)
        # except :
        #     return HttpResponse(0)
        
        return HttpResponse('Check')
    return HttpResponse('Error Add Service!')

@csrf_exempt  
def service(request, id_service):
    if request.method == 'GET':
        return HttpResponse(serialize('json', Service.objects.filter(pk=id_service)), content_type="application/json")
    if request.method == 'POST':
        try:
            is_active = request.POST.get('inputIsActive')
            service = Service.objects.get(id=id_service)
            service.is_active = is_active
            service.save()
            return HttpResponse(1)
        except:
            return HttpResponse(0)
    if request.method == 'DETELE':

        service = Service.objects.get(id=id_service)
        service.is_active = False
        service.save()
        return HttpResponse(1)

    return HttpResponse(0)

# ket thuc tham khao


# Code Category va Attribute dua theo Serive ben duoc comment nay
# Viet funtion nho viet URL va views
def categories(request):
    if request.method == 'GET':
        categories = []
        categories_all = Category.objects.all()
        for item in categories_all:
            category = []
            category.append('<a href="/admin/category/edit/'+ str(item.id) +'">'+ str(item.id) +'</a>'),
            category.append('<a href="/admin/category/edit/'+ str(item.id) +'">'+ str(item.name_category) +'</a>'),         
            category.append(str(item.quantity))
            if item.is_active == True:
                category.append('<b style="color:green">Kích hoạt</b>')
            else:
                category.append('<b style="color:red">Đang khoá</b>')
            categories.append(category)
        return HttpResponse(json.dumps(categories), content_type="application/json")
    return HttpResponse('error')


@csrf_exempt    
def category_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        print(request.POST)
        name_category = request.POST.get('inputName')
        #try:
        category = Category(
            name_category = name_category,
        )
        category.save()
        return HttpResponse(1)
        # except :
        #     return HttpResponse(0)
        return HttpResponse('Check')
    return HttpResponse('Error Add Category!')

@csrf_exempt  
def category(request, id_category):
    if request.method == 'GET':
        return HttpResponse(serialize('json', Category.objects.filter(pk=id_category)), content_type="application/json")
    if request.method == 'POST':
        try:
            name_category = request.POST.get('inputName')
            is_active = request.POST.get('inputIsActive')
            category = Category.objects.get(id=id_category)
            category.name_category = name_category
            category.is_active = is_active
            category.save()
            return HttpResponse(1)
        except:
            return HttpResponse(0)
    if request.method == 'DETELE':
        category = Category.objects.get(id=id_category)
        category.is_active = False
        category.save()
        return HttpResponse(1)

    return HttpResponse(0)



######
######
###### Attribute
######
######
######
######


def attributes(request):
    if request.method == 'GET':
        attributes = []
        attributes_all = Attribute.objects.all()
        for item in attributes_all:
            attribute = []
            attribute.append('<a href="/admin/attribute/edit/'+ str(item.id) +'">'+ str(item.label) +'</a>'),         
            if item.is_active == True:
                attribute.append('<b style="color:green">Có</b>')
            else:
                attribute.append('<b style="color:red">Không</b>')

            attributes.append(attribute)
        return HttpResponse(json.dumps(attributes), content_type="application/json")
    return HttpResponse('error')

@csrf_exempt    
def attribute_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        print(request.POST)
        label = request.POST.get('inputLabel')

        #try:
        attribute = Attribute(
            label = label,
        )
        attribute.save()
        return HttpResponse(1)
        # except :
        #     return HttpResponse(0)
        return HttpResponse('Check')
    return HttpResponse('Error Add !')

@csrf_exempt  
def attribute(request, id_attribute):
    if request.method == 'GET':
        return HttpResponse(serialize('json', Attribute.objects.filter(pk=id_attribute)), content_type="application/json")
    if request.method == 'POST':
        try:

            label = request.POST.get('inputLabel')
            is_active = request.POST.get('inputIsActive')

            attribute = Attribute.objects.get(id=id_attribute)
            attribute.label = label
            attribute.is_active = is_active
            attribute.save()
            return HttpResponse(1)
        except:
            return HttpResponse(0)
    if request.method == 'DETELE':
        Attribute.objects.filter(pk=id_attribute).delete()
        return HttpResponse(1)

    return HttpResponse(0)


####  
####
####
####
####    Account
####
####
####
####

def user(request, id_user):
    if request.method == 'GET':
        if Account.objects.filter(pk=id_user).exists() == True:
            user = Account.objects.get(pk=id_user)
            account = dict()
            account['username']  = user.username
            account['email'] = user.email
            account['name_shop'] = user.name_shop
            account['name']  = user.name
            account['phone'] = user.phone
            account['id_card'] = user.id_card
            account['address'] = user.address
            account['birthday'] = user.birthday

            if user.activity_merchant == True:
                account['role'] = 2
            if user.activity_advertiser == True:
                account['role'] = 3
            if user.activity_account and user.activity_merchant == False:
                account['role'] = 1
            if user.is_admin == True:
                account['role'] = 0

            account['lock'] = user.is_lock
            account['sex'] = user.sex

            return HttpResponse(json.dumps(account), content_type="application/json")
        else:
            return HttpResponse(-3)
    return HttpResponse(-1)


#### Account service

def account_services(request):
    if check_rule(request) == 0:
        return HttpResponse('Quyen truy cap bi tu choi')

    if request.method == 'GET':
        if request.GET.get('service') == 'available':
            if request.GET.get('table') == 'true':
                list_acc_ser = []
                account_services = Account_Service.objects.filter(account__id=request.session.get('user')['id'], remain__gt=0)
                for item in account_services:
                    acc_ser = []
                    acc_ser.append('<a href="/merchant/purchase_service/'+ str(item.service_id) +'"> TD'+ str(item.service_id) +'</a>')
                    acc_ser.append(item.service.service_name)
                    acc_ser.append(str(item.remain)+ ' tin')
                    acc_ser.append(str(item.service.day_limit) + ' ngày')
                    list_acc_ser.append(acc_ser)
                return HttpResponse(json.dumps(list_acc_ser), content_type="application/json")

            account_services = Account_Service.objects.filter(account__id=request.session.get('user')['id'], remain__gt=0)
            list_account_service = []
            for account_service in account_services:
                dict_account_service = dict()
                dict_account_service['post_id'] = account_service.pk
                dict_account_service['account_id'] = account_service.account_id
                dict_account_service['service_id'] = account_service.service_id
                dict_account_service['service_name'] = Service.objects.get(pk=account_service.service_id).service_name
                dict_account_service['remain'] = account_service.remain
                list_account_service.append(dict_account_service)
            return HttpResponse(json.dumps(list_account_service), content_type="application/json")
    return HttpResponse('Error')


######
######
######
######  Prdouct
######
######
######


def products(request):
    if request.method == 'GET':
        if request.GET.get('table') == 'true':
            products = []
            prod_all = Product.objects.filter(type_product=True).order_by('-pk')
            for item in prod_all:
                product = []
                product.append('<a href="/admin/product/see/'+ str(item.id) +'">SP'+ str(item.id) +'</a>')
                product.append(item.name)
                product.append(str(item.price) + ' VND')
                image = Product_Image.objects.filter(product_id_id=item.id).order_by('image_id_id').first()
                product.append('<div class="tbl_thumb_product"><img src="/product/' + image.image_id.image_link.url + '" /></div>')
                if item.consider == 1:
                    product.append('<p style="color:green">Được chấp thuận</p>')
                if item.consider == 0:
                    product.append('<p style="color:red">Bị khóa</p>')
                if item.consider == 2:
                    product.append('<p style="color:blue">Đang xem xét</p>')
                products.append(product)
            return HttpResponse(json.dumps(products), content_type="application/json")
    return

@csrf_exempt  
def product(request, id_product):

    if request.method == 'GET':
        product_detail = dict()
        product_config = Product.objects.filter(id=int(id_product), type_product=True)
        if product_config.count() == 0:
            return HttpResponse(-1)

        product_detail['name'] = product_config[0].name
        product_detail['detail'] = product_config[0].detail
        product_detail['origin'] = product_config[0].origin
        product_detail['code'] = product_config[0].code
        product_detail['price_origin'] = product_config[0].price
        product_detail['consider'] = product_config[0].consider

        product_category = Product_Category.objects.filter(product_id=int(id_product))
        list_category  = []
        for item in product_category:
            category_dict = dict()
            category = Category.objects.get(pk=item.category_id.id)
            category_dict['id'] = category.id
            category_dict['name_category'] = category.name_category
            category_dict['quantity'] = category.quantity
            list_category.append(category_dict)
        product_detail['list_category'] = list_category

        product_image = Product_Image.objects.filter(product_id=int(id_product)).order_by('image_id_id')
        list_image = []
        for item in product_image:
            image_dict = dict()
            image = Image.objects.get(pk=item.image_id.id)
            image_dict['id']  = image.id
            image_dict['image_link'] =  '/product' + image.image_link.url
            image_dict['is_default'] = image.is_default
            image_dict['user_id'] = image.user_id.id
            list_image.append(image_dict)
        product_detail['list_image'] = list_image

        #lay ra danh sach phien ban
        link_type = Link_Type.objects.filter(parent_product=product_config[0].id)
        list_attr = []
        list_price = []
        for item in link_type:
            list_tmp = []
            list_price.append(item.product_id.price)
            product_attr = Product_Attribute.objects.filter(product_id=item.product_id.id).order_by('attribute_id')
            for item in product_attr:
                list_tmp.append(item.value)
            list_attr.append(list_tmp)
    
        #su dung matrix de tra ve danh sach gia tri cho tung thuoc tinh
        len_atr = len(list_attr[0])
        len_verison = len(list_attr)
        list_value_attr = []
        for i in range(len_atr):
            list_temp = []
            for j in range(len_verison):
                if list_attr[j][i] not in list_temp:
                    list_temp.append(list_attr[j][i])
            list_value_attr.append(list_temp)

        product_detail['list_attr'] = list_value_attr
        product_detail['list_price'] = list_price

        return  HttpResponse(json.dumps(product_detail), content_type="application/json")

    #check role
    if request.method == 'POST':
        consider = request.POST.get('consider')
        if Product.objects.filter(pk=id_product).exists() == True:
            product = Product.objects.get(pk=id_product)
            product.consider = consider
            if int(consider) == 1:
                product.is_activity = True
            product.save()
            for item in Link_Type.objects.filter(parent_product=product.id):
                x = item.product_id
                x.consider = consider
                if int(consider) == 1:
                    x.is_activity = True
                x.save()
            return HttpResponse('Thao tac thanh cong!')
    return        
        
####  POST

def posts(request):
    if request.method == 'GET':
        posts = []
        post_all = Post_Product.objects.all()
        for item in post_all:
            post = []
            post.append('<a href="/admin/post/edit/'+ str(item.id) +'"> TD'+ str(item.id) +'</a>'),
            post.append('<a href="/admin/user/see/'+ str(item.creator_id.id) +'">'+ str(item.creator_id.name) +'</a>'),         
            post.append(str(item.quantity - item.bought))
            post.append(item.expire.replace(tzinfo=None).strftime("%d/%m/%Y %H:%M"))
            post.append(item.post_type.service_name)
            if item.is_activity == True:
                post.append('<b style="color:green">Đang hiển thị</b>')
            else:
                post.append('<b style="color:red">Tắt hiển thị</b>')
            posts.append(post)
        return HttpResponse(json.dumps(posts), content_type="application/json")
    return HttpResponse('error')

#### payment

### Ly Thanh 
#Servies Ads Ly Thanh

@csrf_exempt
def getAllPostAds(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')
    if request.method == 'GET':
        result = []
        for item in Service_Ads_Post.objects.filter(purchase_service_id__state=3):
            post_dict = dict()
            post_dict['id'] = item.id
            post_dict['ads_name'] = "<a href='/admin/manager_ads/register_detail/"+str(item.purchase_service_id.id)+"'>"+item.service_name+"</a>"
            post_dict['user'] = item.customer_id.name
            post_dict['date_start']=item.purchase_service_id.date_start.replace(tzinfo=None).strftime("%d/%m/%Y")
            post_dict['position'] = item.purchase_service_id.service_ads_id.position
            post_dict['status'] = "<label class='label label-warning'>Đang chờ</label>"
            result.append(post_dict)
        if result:
            return HttpResponse(json.dumps(result),content_type="application/json")
    
    return HttpResponse(-1)

@csrf_exempt
def getAllAds(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')     
    if request.method == 'GET':
        ads = []
        for item in Service_Ads.objects.all():
            ads_dict = dict()
            ads_dict['service_name'] = "<a href='/admin/manager_ads_detail/"+str(item.pk)+"'>"+item.service_name+"</a>"
            ads_dict['position'] = item.position
            ads_dict['amount'] = item.amount
            ads_dict['day_limit'] = item.day_limit
            if item.is_active:
                ads_dict['is_active'] = "<label class='label label-info'>Kích hoạt</label>"
            else:
                ads_dict['is_active'] = "<label class='label label-warning'>Bị khóa</label>"
            ads.append(ads_dict)
        return  HttpResponse(json.dumps(ads), content_type="application/json")
    return  HttpResponse(1)

@csrf_exempt
def AddService(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')
    if request.method == 'POST':
        _is_active = False
        if request.POST.get('inputStatus') == "Kích hoạt":
            _is_active = True
        _amount = int(request.POST.get('inputAmount').replace(',', ''))
        _date = int(re.sub('\D','',request.POST.get('inpuLimit')))
        obj, created = Service_Ads.objects.update_or_create(
            id = request.POST.get('inputId'),
            defaults = {
                'service_name' : request.POST.get('inputName'),
                'position' : request.POST.get('inputPosition'),
                'amount' : _amount,
                'day_limit' : _date,
                'is_active' : _is_active,
                'creator_id' : 1,
            }
        )
        ads = Service_Ads.objects.filter(service_name=request.POST.get('inputName')).first()
        if ads is None:
            return render(request,'admin/manager_ads/manager_ads_detail.html',{'error':error})
    success = "success"
    return render(request,'admin/manager_ads/manager_ads_detail.html',{'success':success,'ads':obj})
def RemoveService(request,id):
    if check_rule(request) == 0:
        return HttpResponse('Error')
    ads = Service_Ads.objects.filter(id=id).first()
    if ads is None:
        error = "error"
        return render(request,'admin/manager_ads/manager_ads_detail.html',{'error':error})
    else:
        ads.delete()
    success = "success"
    return render(request,'admin/manager_ads/manager_ads.html',{'success':success})

import pytz

@csrf_exempt
def getAllAdsActiving(request):
    input = Purchase_Service_Ads.objects.filter(state=3,is_active=True)
    result = []
    tz = pytz.timezone('Asia/Bangkok')
    now = datetime.now(tz)
    # now = pytz.utc.localize(now)
    for item in input:
        if item.date_start<=now and now<item.date_start+timedelta(days=item.service_ads_id.day_limit):
            ads_dict = dict()
            ads_dict['id'] = item.id
            ads_dict['end'] = (item.date_start+timedelta(days=item.service_ads_id.day_limit)).strftime('%Y-%m-%d-%H-%M-%S')
            #ads_dict['start'] = (item.date_start).strftime('%m-%d-%Y-%H-%M-%S')
            result.append(ads_dict)
    for item in Purchase_Service_Ads.objects.filter(state=2,is_active=True):
        ads_dict = dict()
        ads_dict['id']= "start_"+str(item.id)
        ads_dict['end']=(item.date_start).strftime('%Y-%m-%d-%H-%M-%S')
        result.append(ads_dict)
    if len(result) < 6:
        arr_chose = []
        arr_chose.append("Đầu trang")
        arr_chose.append("Giữa trang")
        arr_chose.append("Cuối trang")
        arr_chose.append("Slide")
        arr_chose.append("Bên phải slide 1")
        arr_chose.append("Bên phải slide 2")
        check = []
        for i in range(6):
            check_dict = dict()
            check_dict['check']=False
            check_dict['key'] = arr_chose[i]
            check.append(check_dict)
        for item in input:
            for i in range(6):
                if item.service_ads_id.position == check[i]['key']:
                    check[i]['check']=True
        for item in check:
            if item['check'] == False:
                ads_dict = dict()
                ads_dict['id']="none_"+item['key']
                ads_dict['end']=(now+timedelta(minutes=30)).strftime('%m-%d-%Y-%H-%M-%S')
                result.append(ads_dict) 
    if result:
        return HttpResponse(json.dumps(result),content_type="application/json")
    return HttpResponse(-1)

@csrf_exempt
def enable_ads(request):
    if request.method == 'POST':
        id = request.POST['inputID']
        service_ads = Purchase_Service_Ads.objects.filter(id=id)
        service_ads.update(state=3)
        return HttpResponse(1)
    return HttpResponse(-1)
@csrf_exempt
def disable_ads(request):
    if request.method == 'POST':
        id = request.POST['inputID']
        service_ads = Purchase_Service_Ads.objects.filter(id=id)
        service_ads.update(state=4)
        return HttpResponse(1)
    return HttpResponse(-1)


### End Ly Thanh

