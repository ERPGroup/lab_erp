from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from website.models import *

from django.contrib import messages
from  passlib.hash import pbkdf2_sha256
from . import functions
from django.core.exceptions import ObjectDoesNotExist

# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser
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

def check_rule(request):
    if 'user' in request.session:
        user = request.session.get('user')
        #print(user['role'])
        if 2 in user['role'] or 3 in user['role']:
            #print(user)
            return 1
        return 0
    return 0

def check_session(request):
    if 'user' in request.session:
        return 1
    return 0
def login (request):
    if check_rule(request) == 1:
        return redirect('/merchant/')
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        try:
            account = Account.objects.get(email=email)
            if pbkdf2_sha256.verify(password, account.password):
                if account.activity_merchant == True or account.activity_advertiser == True:
                    if check_session(request):
                        del request.session['user']
                    request.session['user'] = {
                        'id': account.id,
                        'email': account.email,
                        'role': role_user_session(account),
                    }
                    return redirect('/merchant/login') 
                else:
                    messages.warning(request, message='Tài khoản không được phép truy cập!', extra_tags='alert')
                    return redirect('/merchant/login')
            messages.warning(request, message='Mật khẩu không đúng!', extra_tags='alert')
            return redirect('/merchant/login')
        except ObjectDoesNotExist:
            messages.warning(request, message='Email không tồn tại!', extra_tags='alert')
            return redirect('/merchant/login')
        return
    return render(request, 'merchant/login/Login.html')

def index(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/index.html')


def product(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_product/manager_product.html')

def product_add(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request, 'merchant/manager_product/product_add.html')

def product_edit(request, id_product):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    if Product.objects.filter(pk=int(id_product), type_product=True, account_created_id=request.session.get('user')['id'], archive=False).exists() == False:
        messages.warning(request, message='Sản phẩm không tồn tại', extra_tags='alert')
        return redirect('/merchant')
    return render(request, 'merchant/manager_product/product_edit.html')

## ----- POST product
def posted(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_posted/manager_post.html')

def posted_detail(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_posted/manager_post_detail.html')

def post_add(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_posted/post_add.html')


def post_edit(request, id_post):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    if Post_Product.objects.filter(pk=id_post, creator_id__id=request.session.get('user')['id']).count() == 0:
        messages.warning(request, message='Không tồn tại tin đăng', extra_tags='alert')
        return redirect('/merchant')
    return render(request,'merchant/manager_posted/post_edit.html')

# ------- End

def warehose(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_product/manager_warehose.html')

def order(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_order/manager_order.html')

def order_edit(request, id_order):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    if Order_Detail.objects.filter(order_id=id_order, merchant_id=request.session.get('user')['id']).exists() == False:
        messages.warning(request, message='Không tồn tại đơn hàng', extra_tags='alert')
        return redirect('/merchant')
    return render(request,'merchant/manager_order/manager_order_detail.html')

def statistical_post(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_posted/manager_statistical_post.html')

def rating(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_rating/manager_rating.html')


def payment(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_payment/manager_payment.html')

# def payment_detail(request):
#     if check_rule(request) == 0:
#         return redirect('/merchant/login')
#     return render(request,'merchant/manager_payment/manager_payment_detail.html')

# ---- Service
def service_post(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_service/service_post.html')
    
def purchase_service(request, id_service):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    if Service.objects.filter(pk=id_service, is_active=True).exists() == False:
        messages.warning(request, message='Gói tin không tồn tại hoặc ngừng bán!', extra_tags='alert')
        return redirect('/merchant')
    return render(request,'merchant/manager_service/purchase_service.html')
# ------ End

### Ly Thanh

def service_ads(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    return render(request,'merchant/manager_service/service_ads.html')

def service_ads_register(request,id_ads):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    if functions.get_my_choices(id_ads):
        user = request.session.get('user')
        result = Account.objects.get(pk=user['id'])
        return render(request,'merchant/manager_service/manager_ads_register_detail.html',{ 'list':functions.get_my_choices(id_ads),'user':result })
    else:
        return HttpResponse("Lỗi")

def post_ads(request):
    if check_rule(request) == 0:
        return redirect('/merchant/login')
    user = request.session.get('user')
    result = functions.getServiceAdsAvailable(user['id'])
    return render(request,'merchant/manager_service/service_ads_post.html',{'list':result})

def ads_running(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'merchant/manager_service/manager_ads_running.html')    

def ads_running_detail(request,id):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if id is None:
        return render(request,'merchant/manager_service.html')
    else:
        post_ads = Purchase_Service_Ads.objects.filter(id=id).first()
        return render(request,'merchant/manager_service/manager_ads_running_detail.html',{'result':post_ads})

def payment_ads_detail(request, id_payment):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Purchase_Service_Ads.objects.filter(pk=id_payment).count() == 0:
        messages.warning(request, message='Không tồn tại giao dịch', extra_tags='alert')
        return redirect('/admin/')
    return render(request, 'merchant/manager_payment/payment_ads_detail.html')

def manager_payment_ads(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request, 'merchant/manager_payment/manager_payment_ads.html')



