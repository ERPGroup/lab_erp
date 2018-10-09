from django.shortcuts import render

# Create your views here.
def login (request):
    return render(request, 'login/Login.html')
def index(request):
    return render(request,'admin/index.html')
def users(request):
    return render(request,'admin/manager_users.html')
