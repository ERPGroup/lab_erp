from django.shortcuts import render, redirect
from admin import views
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

def attribute_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        code = request.POST.get('inputCode')
        label = request.POST.get('inputLabel')
        type_attr = request.POST.get('inputTypeAttr')
        is_required = request.POST.get('inputRequired')
        is_unique = request.POST.get('inputUnique')

        try:
            attribute = Attribute(
                code=code,
                lable=label,
                type_attr=type_attr,
                is_required=is_required,
                is_unique=is_unique,
            )
            attribute.save()
            return HttpResponse('Success!')
        except:
            return HttpResponse('Error!')
        
        return HttpResponse('Check')
    return HttpResponse('Error Add Attribute!')

def attribute_edit(request, id_attribute):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        try:
            code = request.POST.get('inputCode')
            label = request.POST.get('inputLabel')
            type_attr = request.POST.get('inputTypeAttr')
            is_required = request.POST.get('inputRequired')
            is_unique = request.POST.get('inputUnique')

            attribute = Attribute.objects.get(id=id_attribute)
            attribute.code = code
            attribute.label = label
            attribute.type_attr = type_attr
            attribute.is_required = is_required
            attribute.is_unique = is_unique

            attribute.save()
            return HttpResponse('Success!')
        except:
            return HttpResponse('Error!')
    return HttpResponse('Error Edit Attribute!')

def attribute_del(request, id_attribute):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        try:
            attribute = Attribute.objects.get(id=id_attribute)
            attribute.delete()
            return HttpResponse('Success!')
        except: 
            return
    return

def category_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == "POST":
        try:
            category = Category(
                name_category=name_category,
                quantity=quantity,
                is_activity=is_activity,
            )
            category.save()
            return HttpResponse('Success!')
        except:
            return
        return
    return

def category_edit(request,id_category):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == "POST":
        try:
            category = Category.objects.get(id=id_category)
            category.name_category = name_category
            category.quantity = quantity
            category.is_activity = is_activity
            category.save()
            return HttpResponse('Success!')
        except:
            return
        return
    return

def category_del(request, id_category):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        try:
            category = Category.objects.get(id=id_category)
            category.delete()
            return HttpResponse('Success!')
        except: 
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

