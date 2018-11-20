from django.shortcuts import render, redirect
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import re
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

#Servies Ads
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

       
