from django.shortcuts import render, redirect
from website.models import * 
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse

def check_session(request):
    if 'user' in request.session:
        return 1
    return 0


def history_order(request):
    if check_session(request)==False:
        messages.warning(request, message='Vui lòng đăng nhập !', extra_tags='alert')
        return redirect('/login')
    order_all = Order.objects.filter(customer_id=request.session.get('user')['id']).order_by('-pk')
    return render(request, 'website/history_order.html', {'data': order_all})

def profile(request):
    if check_session(request)==False:
        messages.warning(request, message='Vui lòng đăng nhập !', extra_tags='alert')
        return redirect('/login')
    
    user = Account.objects.get(pk=request.session.get('user')['id'])
    if user.activity_merchant == True:
        account_role = 'Người bán'
    if user.activity_advertiser == True:
        account_role = 'Người chạy quảng cáo'
    if user.activity_account and user.activity_merchant == False and user.activity_advertiser == False:
        account_role = 'Người mua'
    if user.is_admin == True:
        account_role = 'Admin'
    print(account_role)
    return render(request, 'website/profile.html', {'account_role': account_role,})
    
def bill_detail(request, id_order):
    if check_session(request)==False:
        messages.warning(request, message='Vui lòng đăng nhập !', extra_tags='alert')
        return redirect('/login')
    if Order.objects.filter(customer_id=request.session.get('user')['id'], pk=id_order).exists() == False:
        messages.warning(request, message='Đơn hàng không tồn tại!', extra_tags='alert')
        return redirect('/')
    order = Order.objects.get(customer_id=request.session.get('user')['id'], pk=id_order)
    order_detail = Order_Detail.objects.filter(order_id=order.id)
    print(order_detail)
    # success = True
    # cancel = False
    for item in order_detail:
        item.state_display = item.get_state_display()
        # if item.state != 1:
        #     success = False

    # order.success = success
    # order.cancel = cancel
    list_merchant_id = order_detail.values_list('merchant').distinct()
    merchants = Account.objects.filter(pk__in=list_merchant_id)
    list_rating = []
    for item in merchants:
        count_star = Rating.objects.filter(merchant_id=item.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
        if count_star == None:
            count_star = 0
        count_person = Rating.objects.filter(merchant_id=item.id, is_activity=True).count()
        item.rating = (str(count_star) + ' sao/ '+ str(count_person) +' đánh giá')
    
    return render(request,'website/order_detail.html', {
        'order': order,
        'order_detail': order_detail,
        'merchants': merchants,
    })
