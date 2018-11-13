from django.shortcuts import render

# Create your views here.

from website.models import * 

def change_password(request):
    return

def history_order(request):
    return render(request, 'website/history_order.html')
def profile(request):
    return render(request,'website/profile.html')
def history_order_detail(request):
    return render(request,'website/order_detail.html')

