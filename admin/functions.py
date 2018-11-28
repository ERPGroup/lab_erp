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

# Service_add
@csrf_exempt    
def service_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        service_name = request.POST.get('inputServiceName')
        amount = request.POST.get('inputAmount')
        value = request.POST.get('inputValue')
        day_limit = request.POST.get('inputDayLimit')
        day_visable_page_home = request.POST.get('inputDayVisablePageHome')
        visable_vip = request.POST.get('inputVisableVip')
        is_active = request.POST.get('inputIsActive')
        archive = request.POST.get('inputArchive')

        try:
            service = Service(
                service_name=service_name,
                amount=amount,
                value=value,
                day_limit=day_limit,
                day_visable_page_home=day_visable_page_home,
                visable_vip=visable_vip,
                is_active=is_active,
                archive=archive,
            )
            service.save()
            accounts = Account.objects.all()
            for item in accounts:
                Account_Service.objects.create(
                    account = item,
                    service = service,
                )
            return HttpResponse(1)
        except:
            return HttpResponse(0)
        
        return HttpResponse('Check')
    return HttpResponse('Error Add Service!')

#Servies Ads Ly Thanh
@csrf_exempt
def getAllAds(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')     
    if request.method == 'GET':
        ads = []
        for item in Service_Ads.objects.all():
            ads_dict = dict()
            ads_dict['service_name'] = "<a href='/admin/manager_ads_detail/"+str(item.pk)+"'>"+item.service_name+"</a>"
            ads_dict['type_service'] = item.type_service
            ads_dict['amount'] = item.amount
            ads_dict['day_limit'] = item.day_limit
            if item.is_active:
                ads_dict['is_active'] = "<label class='label label-info'>Kích hoạt</label>"
            else:
                ads_dict['is_active'] = "<label class='label label-warning'>Bị khóa</label>"
            ads.append(ads_dict)
        return  HttpResponse(json.dumps(ads), content_type="application/json")
    return  HttpResponse(1)

#Ly Thanh
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
