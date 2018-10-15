from django.shortcuts import render
from .models import *

# Create your views here.
from django.http import HttpResponse
from  passlib.hash import pbkdf2_sha256

def index (request):
    return HttpResponse("You're looking at question.")


def login (request):
    return render(request, 'website/login.html')


def register (request):
    if request.method  == 'POST':
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        name = request.POST.get('inputFullname')
        new_account = Account(
            email=email,
            password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
            name=name,
        )
        new_account.save()
        return HttpResponse("You're submit form! %s" % email)
    return render(request, 'website/register.html')

