from django.shortcuts import render, redirect
from website import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.files.storage import FileSystemStorage, Storage

import pandas as pd
from datetime import datetime
from datetime import timedelta

import json

@csrf_exempt
def getAds(request):
    key_search = request.POST['key']
    result = Service_Ads_Post.objects.filter(purchase_service_id__is_active=True, purchase_service_id__state=3, purchase_service_id__service_ads_id__position=key_search)
    if result:
        if key_search == "Slide":
            dict_result = dict()
            dict_result['img_1'] = result[0].image_1
            dict_result['url_1'] = result[0].image_1_url
            dict_result['content_1'] = result[0].image_1_content
            dict_result['img_2'] = result[0].image_2
            dict_result['url_2'] = result[0].image_2_url
            dict_result['content_3'] = result[0].image_2_content
            dict_result['img_3'] = result[0].image_3
            dict_result['url_3'] = result[0].image_3_url
            dict_result['content_3'] = result[0].image_3_content
            return HttpResponse(json.dumps(dict_result),content_type="application/json")   
        else:
            dict_result = dict()
            dict_result['img'] = result[0].image_1
            dict_result['url'] = result[0].image_1_url
            dict_result['content'] = result[0].image_1_content
            return HttpResponse(json.dumps(dict_result),content_type="application/json")       
    return HttpResponse(-1)
  