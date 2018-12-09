from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from website.models import *

from django.contrib import messages

from . import functions

# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser
def check_rule(request):
    # if 'user' in request.session:
    #     user = request.session.get('user')
    #     print(user['role'])
    #     if 2 in user['role']:
    #         print(user)
    #         return 1
    #     return 0
    # return 0
    return 1

def login (request):
    if check_rule(request) == 1:
        return redirect('/merchant/index')
    return render(request,'login/Login.html')


def index(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/index.html')


def product(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    

    return render(request,'merchant/manager_product/manager_product.html')

def product_detail(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_product/manager_product_detail.html')

def product_add(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request, 'merchant/manager_product/product_add.html')

def product_edit(request, id_product):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    if Product.objects.filter(pk=int(id_product), type_product=True, account_created_id=request.session.get('user')['id']).exists() == False:
        messages.warning(request, message='Khong ton tai san pham', extra_tags='alert')
        return redirect('/merchant')
    return render(request, 'merchant/manager_product/product_edit.html')

## ----- POST product
def posted(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_posted/manager_post.html')

def posted_detail(request):
    return render(request,'merchant/manager_posted/manager_post_detail.html')

def post_add(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_posted/post_add.html')


def post_edit(request, id_post):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    print(Post_Product.objects.filter(pk=id_post, creator_id_id=request.session.get('user')['id']))
    if Post_Product.objects.filter(pk=id_post, creator_id__id=request.session.get('user')['id']).count() == 0:
        messages.warning(request, message='Khong ton tai tin dang', extra_tags='alert')
        return redirect('/merchant')
    return render(request,'merchant/manager_posted/post_edit.html')

# ------- End

def warehose(request):
    return render(request,'merchant/manager_product/manager_warehose.html')
def order(request):
    return render(request,'merchant/manager_order/manager_order.html')
def order_detail(request):
    return render(request,'merchant/manager_order/manager_order_detail.html')
def statistical_post(request):
    return render(request,'merchant/manager_posted/manager_statistical_post.html')

# ---- Service
def service_post(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_service/service_post.html')
    
def purchase_service(request, id_service):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_service/purchase_service.html')
# ------ End

### Ly Thanh

def service_ads(request):
    return render(request,'merchant/manager_service/service_ads.html')

def service_ads_register(request,id_ads):
    if functions.get_my_choices(id_ads):
        user = request.session.get('user')
        result = Account.objects.get(pk=user['id'])
        return render(request,'merchant/manager_service/manager_ads_register_detail.html',{ 'list':functions.get_my_choices(id_ads),'user':result })
    else:
        return HttpResponse("Loi")

def post_ads(request):
    user = request.session.get('user')
    result = functions.getServiceAdsAvailable(user['id'])
    return render(request,'merchant/manager_service/service_ads_post.html',{'list':result})

def ads_running(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'merchant/manager_service/manager_ads_running.html')    

def ads_running_detail(request,id):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if id is None:
        return render(request,'merchant/manager_service.html')
    else:
        post_ads = Purchase_Service_Ads.objects.filter(id=id).first()
        return render(request,'merchant/manager_service/manager_ads_running_detail.html',{'result':post_ads})


### 

from django import template

