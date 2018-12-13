from django.shortcuts import render, redirect
from django.http import JsonResponse
from website.models import *
# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser

def check_rule(request):
    if 'user' in request.session:
        user = request.session.get('user')
        print(user['role'])
        if 0 in user['role']:
            print(user)
            return 1
        return 0
    return 0

# Create your views here.
def login (request):
    if check_rule(request) == 1:
        return redirect('/admin/index.html')
    return render(request,'login/Login.html')

def index(request):
    if check_rule(request) == 0:
        return redirect('/admin/login')
    return render(request,'admin/index.html')
    
def users(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_users/manager_users.html')

def user_info(request, id_user):
    # check id_user
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Account.objects.filter(pk=id_user).exists() == False:
        messages.warning(request, message='Tài khoản không tồn tại', extra_tags='alert')
        return redirect('/admin/')
    return render(request,'admin/manager_users/user_info.html')

def users_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_users/manager_users_detail.html')




def services(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_servies_post/manager_servies_post.html')

def service_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_servies_post/service_add.html')

def service_edit(request, id_service):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Service.objects.filter(pk=id_service).count() == 0:
        messages.warning(request, message='Gói tin không tồn tại', extra_tags='alert')
        return redirect('/admin/')
    return render(request,'admin/manager_servies_post/service_edit.html')


def post(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_posted/manager_post.html')

def post_detail(request, id_post):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Post_Product.objects.filter(pk=id_post).exists() == False:
        messages.warning(request, message='Tin đăng không tồn tại', extra_tags='alert')
        return redirect('/admin/')
    return render(request,'admin/manager_posted/manager_post_detail.html')

def products(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_product.html')

def products_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_product_detail.html')

def product(request, id_product):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Product.objects.filter(pk=id_product).count() == 0:
        messages.warning(request, message='Sản phẩm không tồn tại', extra_tags='alert')
        return redirect('/admin/')
    return render(request,'admin/manager_product/manager_product_detail.html')


def categories(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/category/manager_categories.html')

def category_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/category/category_add.html')

def category_edit(request,id_category):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Category.objects.filter(pk=id_category).count() == 0:
        messages.warning(request, message='Không tồn tại danh mục', extra_tags='alert')
        return redirect('/admin/')
    return render(request,'admin/manager_product/category/category_edit.html')

def category_detail(request):# function nay khong can sua
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_category_detail.html')

# lam tuong tu Category voi Attribute
# viet view nho viet url, function

def attributes(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/attribute/manager_attributes.html')

def attribute_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/attribute/attribute_add.html')

def attribute_edit(request,id_attribute):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Attribute.objects.filter(pk=id_attribute).count() == 0:
        messages.warning(request, message='Không tồn tại thuộc tính', extra_tags='alert')
        return redirect('/admin/')
    return render(request,'admin/manager_product/attribute/attribute_edit.html')


def manager_attribute_detail(request):# function nay khong can sua
    return render(request,'admin/manager_product/manager_attribute_detail.html')





# ORDER

def manager_order_detail(request, id_order):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Order.objects.filter(pk=id_order).count() == 0:
        messages.warning(request, message='Không tồn tại thuộc tính', extra_tags='alert')
        return redirect('/admin/')
    return render(request, 'admin/manager_order/manager_order_detail.html')

def manager_order(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request, 'admin/manager_order/manager_order.html')

# Payment
def payment_post_detail(request, id_payment):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Purchase_Service.objects.filter(pk=id_payment).count() == 0:
        messages.warning(request, message='Không tồn tại giao dịch', extra_tags='alert')
        return redirect('/admin/')
    return render(request, 'admin/manager_history_pay/payment_post_detail.html')

def manager_payment_post(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request, 'admin/manager_history_pay/manager_payment_post.html')


def payment_ads_detail(request, id_payment):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Purchase_Service_Ads.objects.filter(pk=id_payment).count() == 0:
        messages.warning(request, message='Không tồn tại giao dịch', extra_tags='alert')
        return redirect('/admin/')
    return render(request, 'admin/manager_history_pay/payment_ads_detail.html')

def manager_payment_ads(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request, 'admin/manager_history_pay/manager_payment_ads.html')

def payment(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_history_pay/manager_pay.html')
    
def payment_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_history_pay/manager_pay_detail.html')
    
# Rating

def rating_merchant(request, id_account):
    # check 
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Account.objects.filter(pk=id_user).exists() == False:
        messages.warning(request, message='Tài khoản không tồn tại', extra_tags='alert')
        return redirect('/admin/')
    return render(request, 'admin/manager_rating/manager_rating_mer.html')

def rating_customer(request, id_account):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if Account.objects.filter(pk=id_user).exists() == False:
        messages.warning(request, message='Tài khoản không tồn tại', extra_tags='alert')
        return redirect('/admin/')
    return render(request, 'admin/manager_rating/manager_rating_cus.html')

# -------------------- Ket thuc khu vuc lam viec cua Phuc

def statistical(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/statistical_report/statistical_report.html')


### Thanh Ly - Service Ads
def ads(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads.html')

def ads_created(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    ads = Service_Ads.objects.all().last()
    ads_id = ads.id+1
    return render(request,'admin/manager_ads/manager_ads_detail.html',{'ads_id':ads_id})
    
def ads_detail(request,id):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if id is None:
        return render(request,'admin/manager_ads/manager_ads_detail.html')
    else:
        ads = Service_Ads.objects.filter(id=id).first()
        return render(request,'admin/manager_ads/manager_ads_detail.html', {'ads': ads})

def ads_register(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')

    return render(request,'admin/manager_ads/manager_ads_register.html')

def ads_register_detail(request,id):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if id is None:
        return render(request,'admin/manager_ads_register.html')
    else:
        post_ads = Purchase_Service_Ads.objects.filter(id=id).first()
        return render(request,'admin/manager_ads/manager_ads_register_detail.html',{'result':post_ads})

def ads_running(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_running.html')    

def ads_running_detail(request,id):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    if id is None:
        return render(request,'admin/manager_ads_running.html')
    else:
        post_ads = Purchase_Service_Ads.objects.filter(id=id).first()
        return render(request,'admin/manager_ads/manager_ads_running_detail.html',{'result':post_ads})


### End Thanh Ly
