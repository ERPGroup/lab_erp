from django.shortcuts import render, redirect
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

import json

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
        day_visable_page_home = request.POST.get('inputDayVisablePageHome')
        visable_vip = request.POST.get('inputVisableVip')
        is_active = request.POST.get('inputIsActive')

        #try:
        service = Service(
            service_name=service_name,
            amount=amount,
            value=value,
            quantity_product=quantity_product,
            day_limit=day_limit,
            day_visable_page_home=day_visable_page_home,
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