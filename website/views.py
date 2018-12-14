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


def index (request):
    return render(request, 'website/index.html')


def login (request):
    if check_session(request):
        messages.warning(request, message='Lỗi! Bạn đã đăng nhập hệ thống!', extra_tags='alert')
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
                    messages.success(request, message='Đăng nhập thành công!', extra_tags='alert')
                    return redirect('/') 
                else:
                    return HttpResponse('Vui lòng xác nhận email!')
            return HttpResponse('Mật khẩu không đúng!')
        except ObjectDoesNotExist:
            return HttpResponse('Email không tồn tại!')
        return
    return render(request, 'website/login.html')

def logout (request):
    if check_session(request):
        del request.session['user']
        messages.success(request, message='Đăng xuất thành công!', extra_tags='alert')
        return redirect('/')
    else:
        messages.warning(request, message='Lỗi! Bạn chưa đăng nhập', extra_tags='alert')
        return redirect('/')

def register (request):
    if check_session(request):
        messages.warning(request, message='Lỗi! Bạn đã đăng nhập vào hệ thống', extra_tags='alert')
        return redirect('/')
    return render(request, 'website/register.html')


def activity_account(request, email, code):
    try:
        account = Account.objects.get(email=email)
        if account.activity_account == 1:
            messages.warning(request, message='Lỗi! Tài khoản của bạn đã kích hoạt', extra_tags='alert')
            return redirect('/')
        else:
            if account.code_act_account == code:
                account.activity_account = True
                account.save()

                request.session['user'] = {
                    'id': account.id,
                    'email': account.email,
                    'role': role_user_session(account),
                }
                messages.success(request, message='Tài khoản của bạn đã kích hoạt!', extra_tags='alert')
                return redirect('/')
            else:
                messages.warning(request, message='Lỗi! Mã code không hợp lệ!!', extra_tags='alert')
                return redirect('/')
    except ObjectDoesNotExist:
        messages.warning(request, message='Lỗi! Tài khoản kích hoạt không tồn tại!', extra_tags='alert')
        return redirect('/')
    return 

def activity_merchant(request, email, code):
    try:
        account = Account.objects.get(email=email)
        if account.activity_merchant == 1:
            messages.warning(request, message='Lỗi! Tài khoản của bạn đã kích hoạt bán hàng!', extra_tags='alert')
            return redirect('/')
        else:
            if account.code_act_merchant == code:
                account.activity_merchant = True
                account.activity_account = True
                account.save()
                print(role_user_session(account))
                request.session['user'] = {
                    'id': account.id,
                    'email': account.email,
                    'role': role_user_session(account),
                }
                service_all = Service.objects.all()
                for item in service_all:
                    Account_Service.objects.create(
                        account=account,
                        service=item,
                        remain=0,
                    )

                admin = Account.objects.filter(is_admin=True).first()
                Rating.objects.create(customer=admin, merchant=account, num_of_star=3, confirm_bought=False, is_activity=True)
                messages.success(request, message='Tài khoản của bạn đã kích hoạt!', extra_tags='alert')
                return redirect('/')
            else:
                messages.warning(request, message='Lỗi! Mã code không hợp lệ!!', extra_tags='alert')
                return redirect('/')
    except ObjectDoesNotExist:
        messages.warning(request, message='Lỗi! Tài khoản kích hoạt không tồn tại!', extra_tags='alert')
        return redirect('/')
    return

def activity_ad(request, email, code):
    try:
        account = Account.objects.get(email=email)
        if account.activity_advertiser == 1:
            messages.warning(request, message='Lỗi! Tài khoản của bạn đã kích hoạt quảng cáo!', extra_tags='alert')
            return redirect('/')
        else:
            if account.code_act_ads == code:
                account.activity_advertiser = True
                account.activity_account = True
                account.save()

                print(role_user_session(account))
                request.session['user'] = {
                    'id': account.id,
                    'email': account.email,
                    'role': role_user_session(account),
                }
                
                messages.success(request, message='Tài khoản của bạn đã kích hoạt!', extra_tags='alert')
                return redirect('/')
            else:
                messages.warning(request, message='Lỗi! Mã code không hợp lệ!!', extra_tags='alert')
                return redirect('/')
    except ObjectDoesNotExist:
        messages.warning(request, message='Lỗi! Tài khoản kích hoạt không tồn tại!', extra_tags='alert')
        return redirect('/')
    return


def request_new_password(request, email, code):
    if Account.objects.filter(email=email).exists() == False:
        messages.warning(request, message='Lỗi! Tài khoản không hợp lệ!', extra_tags='alert')
        return redirect('/')
    account = Account.objects.get(email=email)
    if account.code_act_account == code:
        account.activity_account = True
        account.save()

        request.session['user'] = {
            'id': account.id,
            'email': account.email,
            'role': role_user_session(account),
        }
        return redirect('/customer/profile')
    else:
        messages.warning(request, message='Lỗi! Mã code không hợp lệ!!', extra_tags='alert')
        return redirect('/')


# def request_merchant(request):
#     if check_session(request) == 0:
#         return redirect('/login')
#     print(request.session.get('user'))
#     if 2 in request.session.get('user')['role']:
#         messages.warning(request, message='You were a merchant!', extra_tags='alert')
#         return redirect('/')

#     if request.method == 'POST':
#         account = Account.objects.get(email=request.session.get('user')['email'])
#         code = random_code_activity(40)
#         email = account.email
#         account.code_act_merchant = code
#         account.save()
#         send_mail_register('activity_merchant', email, code)
#         messages.success(request, message='Request Success! Please check email!', extra_tags='alert')
#         return redirect('/')
#     return render(request, 'website/request_merchant.html')


def search(request, id_account):
    return

def shop(request, id_account):
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
    