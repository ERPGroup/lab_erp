from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

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