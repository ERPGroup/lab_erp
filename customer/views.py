from django.shortcuts import render, redirect
from website.models import * 
from django.contrib import messages

def check_session(request):
    if 'user' in request.session:
        return 1
    return 0


def history_order(request):
    return render(request, 'website/history_order.html')

def profile(request):
    if check_session(request)==False:
        messages.warning(request, message='Please login !', extra_tags='alert')
        return redirect('/login/')
    return render(request,'website/profile.html')
    
def history_order_detail(request):
    return render(request,'website/order_detail.html')

