from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from website.models import *

# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser
def check_rule(request):
    if 'user' in request.session:
        user = request.session.get('user')
        print(user['role'])
        if 2 in user['role']:
            print(user)
            return 1
        return 0
    return 0

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
    if request.method == "POST":

        
        product = Product(
            name=name,
            detail=detail,
            origin=origin,
            type_product=type_product,
            is_visible=is_visible,
            is_activity=is_activity,
            archive=archive,
            account_created=account_created,
        )
        product.save()
        
        list_category = request.POST.get('inputCategory')
        for item in list_category:
            product_category = Product_Category(
                product_id = product.id,
                category_id = item
            )
            product_category.save()

        list_attr = request.POST.get('inputAttribute')
        value = request.POST.get('inputAttribute')  #edit input
        for item in list_attr:
            product_attr = Product_Attribute(
                product_id=product.id,
                attribute_id=item,
                value=value,
            )
            product_attr.save()

        list_images = request.POST.get('inputAttribute') #edit input
        image_link = request.POST.get('inputAttribute') #edit input
        is_default = request.POST.get('inputAttribute') #edit input
        for item in list_images:
            image = Image(
                product_id = product.id,
                image_link = image_link,
                is_default = is_default,
            )
            image.save()


        percent = request.POST.get('inputAttribute') #edit input
        date_start = request.POST.get('inputAttribute')  #edit input
        date_end = request.POST.get('inputAttribute')  #edit input
        discount = Discount(
            product_id=product.id,
            percent=percent,
            date_start=date_start,
            date_end=date_end,
        )

        
        return
    return 




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
    return render(request,'merchant/manager_service/service_post.html')
def service_ads(request):
    return render(request,'merchant/manager_service/service_ads.html')
def service_ads_register(request):
    return render(request,'merchant/manager_service/manager_ads_register_detail.html')
from django import template

