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