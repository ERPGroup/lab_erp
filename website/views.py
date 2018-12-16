import random
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Sum

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
                    if account.activity_merchant == True or account.activity_advertiser == True or account.is_admin == True:
                        messages.warning(request, message='Tài khoản không tồn tại!', extra_tags='alert')
                        return redirect('/login')
                    request.session['user'] = {
                        'id': account.id,
                        'email': account.email,
                        'role': role_user_session(account),
                    }
                    messages.success(request, message='Đăng nhập thành công!', extra_tags='alert')
                    return redirect('/customer/profile') 
                else:
                    messages.warning(request, message='Vui lòng xác nhận email!', extra_tags='alert')
                    return redirect('/login')
            messages.warning(request, message='Mật khẩu không đúng!', extra_tags='alert')
            return redirect('/login')
        except ObjectDoesNotExist:
            messages.warning(request, message='Email không tồn tại!', extra_tags='alert')
            return redirect('/login')
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


#Product - collection - detail 
def detail_post(request, id_post):
    if Post_Product.objects.filter(pk=id_post, is_lock=False, is_activity=True).exists() == False:
        messages.warning(request, message='Tin dang khong ton tai', extra_tags='alert')
        return redirect('/')

    

    
    post = Post_Product.objects.filter(pk=id_post, is_lock=False, is_activity=True).first()
    view_old = post.views
    post.views = view_old + 1
    post.save()

    rating = dict()
    count_star = Rating.objects.filter(merchant_id=post.creator_id.id).aggregate(Sum('num_of_star'))['num_of_star__sum']
    star_5 = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True, num_of_star=5).count()
    star_4 = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True, num_of_star=4).count()
    star_3 = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True, num_of_star=3).count()
    star_2 = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True, num_of_star=2).count()
    star_1 = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True, num_of_star=1).count()
    if count_star == None:
        count_star = 0
    count_person = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
    if count_person == 0:
        rating['agv_rating'] = 0
    else:
        rating['agv_rating'] = float(count_star/count_person)
    if count_person != 0:
        rating['star_5'] = [star_5, (star_5/count_person) *100]
        rating['star_4'] = [star_4, (star_4/count_person) *100]
        rating['star_3'] = [star_3, (star_3/count_person) *100]
        rating['star_2'] = [star_2, (star_2/count_person) *100]
        rating['star_1'] = [star_1, (star_1/count_person) *100]

        list_color = []
        for i in range(0, int(count_star/count_person)):
            list_color.append(1)
        for j in range(0, 5 - int(count_star/count_person)):
            list_color.append(0)

        rating['list_color'] = list_color
    # rating['star_g'] = 5 - int(count_star/count_person)
    list_rating = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).order_by('-pk')
    for item in list_rating:
        if item.num_of_star == 1:
            item.list_color = [1,0,0,0,0]
        if item.num_of_star == 2:
            item.list_color = [1,1,0,0,0]
        if item.num_of_star == 3:
            item.list_color = [1,1,1,0,0]
        if item.num_of_star == 4:
            item.list_color = [1,1,1,1,0]
        if item.num_of_star == 5:
            item.list_color = [1,1,1,1,1]
    rating['list_rating'] = list_rating

    product_category = Product_Category.objects.filter(product_id=post.product_id.id, archive=False).first()
    category = product_category.category_id
    list_poduct_avaliable = Product_Category.objects.filter(archive=False, category_id_id=category.id).values_list('product_id_id')
    list_post = Post_Product.objects.filter(is_lock=False, is_activity=True, product_id_id__in=list_poduct_avaliable).order_by('-bought')[0:40]
    list_random = []
    while len(list_random) >= 4:
        x = randint(0, list_post.count() - 1)
        if x not in list_random:
            list_random.append(x)
    if list_post.count() < 5:
        posts = list_post
    else:
        posts = [list_post[list_random[0]], list_post[list_random[1]], list_post[list_random[2]], list_post[list_random[3]]]
    # print(posts)
    array_post = []
    for post in posts:
        dict_post = post.__dict__
        count_star = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).aggregate(Sum('num_of_star'))['num_of_star__sum']
        if count_star == None:
            count_star = 0
        count_person = Rating.objects.filter(merchant_id=post.creator_id.id, is_activity=True).count()
        if count_person == 0:
            dict_post['rating'] = float(0)
        else:
            dict_post['rating'] = float(round(count_star/count_person, 1))

        del dict_post['_state']
        # if Product.objects.filter(pk=post.id).exists() == True:
        dict_product = Product.objects.get(pk=post.product_id_id).__dict__
        list_price = Link_Type.objects.filter(parent_product=dict_product['id'], product_id__archive=False).values_list('product_id__price')
        dict_product['range_price'] = [max(list_price)[0], min(list_price)[0]]
        del dict_product['_state']
        image = Product_Image.objects.filter(product_id_id=dict_product['id']).order_by('image_id_id').first()
        dict_product['image'] = 'http://localhost:8000/product' + image.image_id.image_link.url
        dict_post['product'] = dict_product
        array_post.append(dict_post)
    
    return render(request,'website/product.html', {'rating': rating, 'array_post': array_post}) 
 
def collections(request, id_category): 
    if Category.objects.filter(pk=id_category).exists() == False:
        messages.warning(request, message='Category khong ton tai', extra_tags='alert')
        return redirect('/')
    return render(request,'website/collection.html')

def search(request):
    if 'r' not in request.GET:
        messages.warning(request, message='Vui lòng nhập từ khóa!', extra_tags='alert')
        return redirect('/')
    return render(request, 'website/search.html')

def shop(request, id_shop):
    if Account.objects.filter(pk=id_shop, activity_merchant=True, is_lock=False).exists() == False:
        messages.warning(request, message='Cửa hàng không tồn tại!', extra_tags='alert')
        return redirect('/')
    
    account = Account.objects.filter(pk=id_shop, activity_merchant=True, is_lock=False).first()
    rating = dict()
    count_star = Rating.objects.filter(merchant_id=account.id).aggregate(Sum('num_of_star'))['num_of_star__sum']
    star_5 = Rating.objects.filter(merchant_id=account.id, is_activity=True, num_of_star=5).count()
    star_4 = Rating.objects.filter(merchant_id=account.id, is_activity=True, num_of_star=4).count()
    star_3 = Rating.objects.filter(merchant_id=account.id, is_activity=True, num_of_star=3).count()
    star_2 = Rating.objects.filter(merchant_id=account.id, is_activity=True, num_of_star=2).count()
    star_1 = Rating.objects.filter(merchant_id=account.id, is_activity=True, num_of_star=1).count()
    if count_star == None:
        count_star = 0
    count_person = Rating.objects.filter(merchant_id=account.id, is_activity=True).count()
    if count_person == 0:
        rating['agv_rating'] = 0
    else:
        rating['agv_rating'] = float(count_star/count_person)
    if count_person != 0:
        rating['star_5'] = [star_5, (star_5/count_person) *100]
        rating['star_4'] = [star_4, (star_4/count_person) *100]
        rating['star_3'] = [star_3, (star_3/count_person) *100]
        rating['star_2'] = [star_2, (star_2/count_person) *100]
        rating['star_1'] = [star_1, (star_1/count_person) *100]

        list_color = []
        for i in range(0, int(count_star/count_person)):
            list_color.append(1)
        for j in range(0, 5 - int(count_star/count_person)):
            list_color.append(0)

        rating['list_color'] = list_color
    # rating['star_g'] = 5 - int(count_star/count_person)
    list_rating = Rating.objects.filter(merchant_id=account.id, is_activity=True).order_by('-pk')
    for item in list_rating:
        if item.num_of_star == 1:
            item.list_color = [1,0,0,0,0]
        if item.num_of_star == 2:
            item.list_color = [1,1,0,0,0]
        if item.num_of_star == 3:
            item.list_color = [1,1,1,0,0]
        if item.num_of_star == 4:
            item.list_color = [1,1,1,1,0]
        if item.num_of_star == 5:
            item.list_color = [1,1,1,1,1]
    rating['list_rating'] = list_rating
    return render(request, 'website/shop.html', {'rating': rating})
 
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

def product(request):
    return render(request,'website/product.html')