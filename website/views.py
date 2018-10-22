import random
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
from django.http import HttpResponse
from  passlib.hash import pbkdf2_sha256
from sender import Mail, Message


def random_code_activity(length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

def index (request):
    return render(request, 'website/index.html')


def login (request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        try:
            account = Account.objects.get(email=email)
            if pbkdf2_sha256.verify(password, account.password):
                if account.activity_account == True:
                    return redirect('/') 
                else:
                    return HttpResponse('You dont active email!')
        except:
            return HttpResponse("Wrong!")
        return
    return render(request, 'website/login.html')


def register (request):
    if request.method  == 'POST':
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        name = request.POST.get('inputFullname')
        code = random_code_activity(40)
        new_account = Account(
            email=email,
            password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
            name=name,
            code_act_account=code,
        )
        new_account.save()
        try:
            mail = Mail(
                'smtp.gmail.com', 
                port='465', 
                username='dinhtai018@gmail.com', 
                password='wcyfglkfcshkxoaa',
                use_ssl=True,
                use_tls=False,
                debug_level=False
            )
            msg = Message('Register Website c2c')
            msg.fromaddr = ("Website C2C", "dinhtai018@gmail.com")
            msg.to = email
            msg.body = "This is email activity account!"
            msg.html = '<h1>THis link activity: <a href="http://localhost:8000/activity/%s">Verify</a></h1>' % code
            msg.reply_to = 'no-reply@gmail.com'
            msg.charset = 'utf-8'
            msg.extra_headers = {}
            msg.mail_options = []
            msg.rcpt_options = []
            mail.send(msg)
        except:
            print('error')
        
        return HttpResponse("You're submit form! %s" % email)
    return render(request, 'website/register.html')

<<<<<<< Updated upstream
=======
def activity_account(request, code):
    try:
        account = Account.objects.get(code_act_account=code, activity_account=False)
        account.activity_account = True
        account.save()
    except DoesNotExists:
        return HttpResponse('NOT activity!')
    return 

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')

    return

def change_password(request):
    return

def category_product(request):
    return

def cart (request):
    return

>>>>>>> Stashed changes
