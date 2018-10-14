from django.shortcuts import render
from admin import views
# Create your views here.
def login (request):
    return render(request,'login/Login.html')
def index(request):
    return render(request,'merchant/index.html')
def product(request):
    return render(request,'merchant/manager_product/manager_product.html')
def product_detail(request):
    return render(request,'merchant/manager_product/manager_product_detail.html')
def posted(request):
    return render(request,'merchant/manager_posted/manager_post.html')
def posted_detail(request):
    return render(request,'merchant/manager_posted/manager_post_detail.html')
def warehose(request):
    return render(request,'merchant/manager_product/manager_warehose.html')