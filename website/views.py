import random
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
from django.http import HttpResponse
from  passlib.hash import pbkdf2_sha256
from sender import Mail, Message
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from cart.cart import Cart


def check_session(request):
    if 'user' in request.session:
        return 1
    return 0

def role_user_session(account):
    # account = Account.objects.get(email=email)
    role = []
    if account.is_admin:
        role.append(0)
    if account.activity_account:
        role.append(1)
    if account.activity_merchant:
        role.append(2)
    if account.activity_advertiser:
        role.append(3)
    return role

def random_code_activity(length):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

def index (request):
    return render(request, 'website/index.html')


def login (request):
    if check_session(request):
        messages.warning(request, message='You were login system', extra_tags='alert')
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        try:
            account = Account.objects.get(email=email)
            if pbkdf2_sha256.verify(password, account.password):
                if account.activity_account == True:
                    request.session['user'] = {
                        'id': account.id,
                        'email': account.email,
                        'role': role_user_session(account),
                    }
                    messages.success(request, message='Login Success!', extra_tags='alert')
                    return redirect('/') 
                else:
                    return HttpResponse('You dont active email!')
            return HttpResponse('Wrong Pass')
        except ObjectDoesNotExist:
            return HttpResponse('Wrong Email!')
        return
    return render(request, 'website/login.html')

def logout (request):
    if check_session(request):
        del request.session['user']
        messages.success(request, message='Logout Success!', extra_tags='alert')
        return redirect('/')
    else:
        messages.warning(request, message='You didnt login', extra_tags='alert')
        return redirect('/')

def register (request):
    if check_session(request):
        messages.warning(request, message='You were login system', extra_tags='alert')
        return redirect('/')

    if request.method  == 'POST':
        username = request.POST.get('inputUsername')
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        name = request.POST.get('inputFullname')
        
        option_acc = request.POST.get('inputOptionAcc')
        if int(option_acc) == 0:
            code = random_code_activity(40)
            new_account = Account(
                username = username,
                email=email,
                password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
                name=name,
                code_act_account=code,
            )
            new_account.save()
            send_mail_register('activity', email, code)

        elif int(option_acc) == 1:
            cmnd = request.POST.get('inputID')
            phone = request.POST.get('inputTel')
            address = request.POST.get('inputAddress')
            store = request.POST.get('inputStore')
            code_act_merchant = random_code_activity(40)
            new_account = Account(
                username = username,
                email = email,
                password = pbkdf2_sha256.encrypt(password, rounds=1200, salt_size=32),
                name=name,
                code_act_merchant=code_act_merchant,
                activity_account=True,
                id_card=cmnd,
                phone=phone,
                address=address,    
                name_shop=store,
            )
            new_account.save()
            send_mail_register('activity_merchant', email, code_act_merchant)
        elif int(option_acc) == 2:
            code_act_ads = random_code_activity(40)
        
        return HttpResponse("You're submit form! %s" % email)
    return render(request, 'website/register.html')

def send_mail_register(slug_url, email, code):
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
        msg.html = '<h1>This link activity: <a href="http://localhost:8000/%s/%s/%s/">Verify</a></h1>' % (slug_url, email, code)
        msg.reply_to = 'no-reply@gmail.com'
        msg.charset = 'utf-8'
        msg.extra_headers = {}
        msg.mail_options = []
        msg.rcpt_options = []
        mail.send(msg)
    except:
        print('error')

def activity_account(request, email, code):
    try:
        account = Account.objects.get(email=email)
        if account.activity_account == 1:
            return HttpResponse('You actived your account')
        else:
            if account.code_act_account == code:

                account.activity_account = True
                account.save()

                account = Account.objects.get(email=email)
                request.session['user'] = {
                    'id': account.id,
                    'email': account.email,
                    'role': role_user_session(account),
                }
                return HttpResponse('Okay!')
            else:
                return HttpResponse('Wrong!')
    except ObjectDoesNotExist:
        return HttpResponse('NOT activity!')
    return 

def request_new_password(request):
    email = request.POST.get('forgot_email')
    try:
        account = Account.objects.get(email=email)
        return HttpResponse('Da gui thong tin qua email')
    except ObjectDoesNotExist:
        return HttpResponse('Email khong ton tai')
    return

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
    return

def change_password(request):
    return

def category_product(request):
    return


def request_merchant(request):
    if check_session(request) == 0:
        return redirect('/login')

    print(request.session.get('user'))

    if 2 in request.session.get('user')['role']:
        messages.warning(request, message='You were a merchant!', extra_tags='alert')
        return redirect('/')

    if request.method == 'POST':
        

        account = Account.objects.get(email=request.session.get('user')['email'])

        code = random_code_activity(40)
        email = account.email

        account.code_act_merchant = code
        account.save()
        send_mail_register('activity_merchant', email, code)
        messages.success(request, message='Request Success! Please check email!', extra_tags='alert')
        return redirect('/')
    return render(request, 'website/request_merchant.html')


#Can them cac dich vu cho tai khoan nguoi ban
def activity_merchant(request, email, code):
    try:
        account = Account.objects.get(email=email)
        if account.activity_merchant == 1:
            return HttpResponse('You actived your merchant')
        else:
            if account.code_act_merchant == code:
                account.activity_merchant = True
                account.save()

                account = Account.objects.get(email=email)
                print(role_user_session(account))
                request.session['user'] = {
                    'id': account.id,
                    'email': account.email,
                    'role': role_user_session(account),
                }
                return HttpResponse('Okay!')
            else:
                return HttpResponse('Wrong!')
    except ObjectDoesNotExist:
        return HttpResponse('NOT activity!')
    return

def resend_code(request):
    return



#Product - collection - detail 
def detail_post(request, id_post):
    if Post_Product.objects.filter(pk=id_post, is_lock=False, is_activity=True).exists() == False:
        messages.warning(request, message='Product khong ton tai', extra_tags='alert')
        return redirect('/')
    return render(request,'website/product.html') 
 
def collections(request, id_category): 
    if Category.objects.filter(pk=id_category).exists() == False:
        messages.warning(request, message='Category khong ton tai', extra_tags='alert')
        return redirect('/')
    return render(request,'website/collection.html')
 
def checkout(request): 
    if 'user' in request.session:
        cart = Cart(request.session)
        if cart.count == 0:
            messages.warning(request, message='Bạn chưa có sản phẩm nào trong giỏ hàng', extra_tags='alert')
            return redirect('/')
        account = Account.objects.get(pk=request.session.get('user')['id'])
        return render(request,'website/checkout.html', {
            'account': account,
        })
    else:
        messages.warning(request, message='Vui lòng đăng nhập để thanh toán', extra_tags='alert')
        return redirect('/')
 
# def profile(request): 
#     return render(request,'website/checkout') 
 
def cart(request):
    if 'user' in request.session:
        return render(request,'website/cart.html')
    else:
        messages.warning(request, message='Vui lòng đăng nhập để mua hàng', extra_tags='alert')
        return redirect('/')
    