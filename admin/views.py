from django.shortcuts import render, redirect
from django.http import JsonResponse
from website.models import *
# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser

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

# Create your views here.
def login (request):
    if check_rule(request) == 1:
        return redirect('/admin/index')
    return render(request,'login/Login.html')

def index(request):
    if check_rule(request) == 0:
        return redirect('/admin/login')
    return render(request,'admin/index.html')
    
def users(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_users/manager_users.html')

def users_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_users/manager_users_detail.html')

def servies(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_servies_post/manager_servies_post.html')

def servies_add(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_servies_post/service_add.html')

def payment(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_history_pay/manager_pay.html')
    
def payment_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_history_pay/manager_pay_detail.html')

def post(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_posted/manager_post.html')

def post_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_posted/manager_post_detail.html')

def ads(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads.html')
    
def ads_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_detail.html')

def ads_register(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_register.html')

def ads_register_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_ads/manager_ads_register_detail.html')
    
def products(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_product.html')

def products_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_product_detail.html')

def categories(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_category.html')

def category_detail(request):
    if check_rule(request) == 0:         
        return redirect('/admin/login')
    return render(request,'admin/manager_product/manager_category_detail.html')
def manager_attribute(request):
    return render(request,'admin/manager_product/manager_attribute.html')
def manager_attribute_detail(request):
    return render(request,'admin/manager_product/manager_attribute_detail.html')

def statistical(request):
    return render(request,'admin/statistical_report/statistical_report.html')


# def get_last_ads(id):
#     #Lấy quảng cáo có thời gian bắt đầu nhỏ nhất trong hợp đồng, theo ma quang cao.  
#     return
# def get_ads_current(id):
#     #Lấy quảng cáo hiện tại theo mã quảng cáo
#     return
# def update_ads(request):
#     if request.method == "POST":
#         id_ads = request.POST.get('id_ads')
#         current_ads = get_ads_current(id_ads)
#         new_ads = get_last_ads(id_ads)
#         #Cap nhap quang cao hien tai. thay the' bang quang cao tiep theo
#         current_ads = new_ads
#         return JsonResponse(new_ads.TenQuangCao)
