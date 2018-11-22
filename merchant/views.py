from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from website.models import *
from . import functions
from django.contrib import messages

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
    if Product.objects.filter(pk=int(id_product), type_product=True).count() == 0:
        messages.warning(request, message='Khong ton tai san pham', extra_tags='alert')
        return redirect('/merchant/')
    return render(request, 'merchant/manager_product/product_edit.html')


def posted(request):
    return render(request,'merchant/manager_posted/manager_post.html')
def posted_detail(request):
    return render(request,'merchant/manager_posted/manager_post_detail.html')
def warehose(request):
    return render(request,'merchant/manager_product/manager_warehose.html')
def order(request):
    return render(request,'merchant/manager_order/manager_pay.html')
def order_detail(request):
    return render(request,'merchant/manager_order/manager_pay_detail.html')
def statistical_post(request):
    return render(request,'merchant/manager_posted/manager_statistical_post.html')
    
def service_post(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_service/service_post.html')
    
def purchase_service(request, id_service):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_service/purchase_service.html')

def service_ads(request):
    return render(request,'merchant/manager_service/service_ads.html')

def service_ads_register(request,id_ads):
    if functions.get_my_choices(id_ads):
        return render(request,'merchant/manager_service/manager_ads_register_detail.html',{ 'list':functions.get_my_choices(id_ads) })
    else:
        return HttpResponse("Loi")

def post_ads(request):
    user = request.session.get('user')
    result = functions.getServiceAdsAvailable(user['id'])
    return render(request,'merchant/manager_service/service_ads_post.html',{'list':result})

from django import template

