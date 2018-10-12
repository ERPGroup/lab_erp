from django.shortcuts import render
from admin import views
# Create your views here.
def login (request):
    return render(request,'login/Login.html')
def index(request):
    return render(request,'merchant/index.html')