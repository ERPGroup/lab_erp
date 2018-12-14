from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
from django.http import HttpResponse, Http404
from passlib.hash import pbkdf2_sha256
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict


import os
from django.conf import settings
import pdfkit



def success_order(request, id_order):
    if request.method == 'GET':
        if Order.objects.filter(pk=id_order, customer_id=request.session.get('user')['id']).exists() == False:
            return HttpResponse('Đơn hàng không tồn tại')
        order = Order.objects.get(pk=id_order, customer_id=request.session.get('user')['id'])
        if order.state == '1':
            return HttpResponse('Lỗi! Đơn hàng đã hoàn thành trước đó')
        order_items_check_state = Order_Detail.objects.filter(order_id=id_order).values_list('state')
        if '2' in order_items_check_state:
            return HttpResponse('Không được phép thay đổi')
        if '3' in order_items_check_state:
            return HttpResponse('Không được phép thay đổi')
        if '4' in order_items_check_state:
            return HttpResponse('Không được phép thay đổi')
        order.state == '1'
        order.save()
        return HttpResponse(1)

def cancel_order(request, id_order):
    if request.method == 'GET':
        if Order.objects.filter(pk=id_order, customer_id=request.session.get('user')['id']).exists() == False:
            return HttpResponse('Đơn hàng không tồn tại')
        order = Order.objects.get(pk=id_order, customer_id=request.session.get('user')['id'])
        if order.state == '0':
            return HttpResponse('Lỗi! Đơn hàng đã bị hủy trước đó')
        order_items_check_state = Order_Detail.objects.filter(order_id=id_order).values_list('state')
        if '1' in order_items_check_state:
            return HttpResponse('Không được phép thay đổi')
        
        order_item = Order_Detail.objects.filter(order_id=id_order)
        for item in order_item:
            post = Post_Product.objects.filter(pk=item.post.id).first()
            bought = post.bought
            post.bought = bought - item.quantity
            if post.is_lock == True:
                post.is_lock = False
            post.save()

        order.state == '0'
        order.save()
        return HttpResponse(1)

def cancel_order_item(request, id_order_item):
    if request.method == 'GET':
        if Order_Detail.objects.filter(pk=id_order_item).exists() == False:
            return HttpResponse('Không tồn tại món hàng này!')
        order_detail = Order_Detail.objects.get(pk=id_order_item)
        if order_detail.state == '0':
            return HttpResponse('Lỗi! Món hàng đã bị hủy trước đó')
        quantity = order_detail.quantity
        order_detail.state = '0'
        order_detail.canceler_id = Account.objects.get(pk=request.session.get('user')['id'])
        order_detail.save()
        post = Post_Product.objects.filter(pk=order_detail.post.id).first()
        bought = post.bought
        post.bought = bought - quantity
        if post.is_lock == True:
            post.is_lock = False
        post.save()
        return HttpResponse(1)



# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404

# @csrf_exempt  
# def print_bill(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         output = request.POST.get('output')
#         file_path = os.path.join(settings.MEDIA_ROOT, '/bill/' + output)
#         if os.path.exists('/bill/' + file_path):
#             download(request, file_path)
#             return HttpResponse(1)
#         else:
#             pdfkit.from_string(url, file_path)
#             download(request, file_path)
#             return HttpResponse(1)
#     return HttpResponse(503)

@csrf_exempt  
def profile(request):
    if request.method == 'GET':
        return HttpResponse(serialize('json', Account.objects.filter(pk=request.session.get('user')['id'])), content_type="application/json")

@csrf_exempt  
def change_pw(request):
    if request.method == 'POST':
        try:
            password = request.POST.get('inputPassword')
            account = Account.objects.get(email=request.session.get('user')['email'])
            account.password = pbkdf2_sha256.hash(password)     
            account.save()
            return HttpResponse(1)
        except:
            return HttpResponse(0)
    return HttpResponse(0)

@csrf_exempt  
def change_info(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            birthday = request.POST.get('birthday')
            sex = request.POST.get('sex')

            account = Account.objects.get(email=request.session.get('user')['email'])
            account.name = name
            account.address = address
            account.phone = phone
            account.birthday = birthday
            account.sex = sex

            account.save()
            return HttpResponse(1)
        except:
            return HttpResponse(0)
    return HttpResponse(0)

# def get_orders(request):
#     if request.method == 'GET':
#         list_order = []
#         order_all = Order.objects.filter(customer_id=request.session.get('user')['id'])
#         for item in order_all:
#             list_order.append(model_to_dict(item))
#         return HttpResponse(json.dumps({'data' : list_order}, sort_keys=False, indent=1, cls=DjangoJSONEncoder), content_type="application/json")
 