from django.shortcuts import render, redirect
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.files.storage import FileSystemStorage, Storage

from datetime import datetime, timedelta
from django.utils import timezone
import pytz
import json, os

# 0 Admin, 1 Customer, 2 Merchant, 3 Advertiser
def check_rule(request):
    if 'user' in request.session:
        user = request.session.get('user')
        print(user['role'])
        if 2 in user['role']:
            print(user)
            return 1
        return 0
    return 0


############
#############
###########
############
############
####
####
########

def account_services(request):
    if check_rule(request) == 0:
        return HttpResponse('Quyen truy cap bi tu choi')

    if request.method == 'GET':
        if request.GET.get('service') == 'available':
            if request.GET.get('table') == 'true':
                list_acc_ser = []
                account_services = Account_Service.objects.filter(account__id=request.session.get('user')['id'], remain__gt=0)
                for item in account_services:
                    acc_ser = []
                    acc_ser.append('<a href="/merchant/purchase_service/'+ str(item.service_id) +'"> TD'+ str(item.service_id) +'</a>')
                    acc_ser.append(item.service.service_name)
                    acc_ser.append(str(item.remain)+ ' tin')
                    acc_ser.append(str(item.service.day_limit) + ' ngày')
                    list_acc_ser.append(acc_ser)
                return HttpResponse(json.dumps(list_acc_ser), content_type="application/json")

            account_services = Account_Service.objects.filter(account__id=request.session.get('user')['id'], remain__gt=0)
            list_account_service = []
            for account_service in account_services:
                dict_account_service = dict()
                dict_account_service['post_id'] = account_service.pk
                dict_account_service['account_id'] = account_service.account_id
                dict_account_service['service_id'] = account_service.service_id
                dict_account_service['service_name'] = Service.objects.get(pk=account_service.service_id).service_name
                dict_account_service['remain'] = account_service.remain
                list_account_service.append(dict_account_service)
            return HttpResponse(json.dumps(list_account_service), content_type="application/json")
    return HttpResponse('Error')



####
####
####
####
####
####
####
####
####
####
####
####
####
####

def categorys(request):
    return HttpResponse(serialize('json', Category.objects.all()), content_type="application/json")

def category(request, id_category):
    if request.method == "GET":
        return HttpResponse(serialize('json', Category.objects.filter(pk=id_category)), content_type="application/json")

    if check_rule(request) == 0:
        return HttpResponse('Error')
    else:

        # Edit Category
        if request.method == "PATCH":
            try:
                name_category = request.POST.get('inputNameCategory')
                quantity = request.POST.get('inputQuantity')
                category = Category.objects.get(id=id_category)
                category.name_category = name_category
                category.quantity = quantity
                category.save()
                return HttpResponse('Success!')
            except:
                return
            return
        return

        #Delete Category
        if request.method == 'DELETE':
            try:
                category = Category.objects.get(id=id_category)
                category.delete()
                return HttpResponse('Success!')
            except: 
                return
        return



# @csrf_exempt
def category_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == "POST":
        name_category = request.POST.get('inputNameCategory')
        quantity = request.POST.get('inputQuantity')
        try:
            category = Category(
                name_category=name_category,
                quantity=quantity,
            )
            category.save()
            return HttpResponse('Success!')
        except:
            return
        return
    return

# def category_edit(request,id_category):
#     if check_rule(request) == 0:
#         return HttpResponse('Error')

#     if request.method == "PUT":
#         try:
#             name_category = request.POST.get('inputNameCategory')
#             quantity = request.POST.get('inputQuantity')
#             category = Category.objects.get(id=id_category)
#             category.name_category = name_category
#             category.quantity = quantity
#             category.save()
#             return HttpResponse('Success!')
#         except:
#             return
#         return
#     return

# def category_del(request, id_category):
#     if check_rule(request) == 0:
#         return HttpResponse('Error')

#     if request.method == 'DELETE':
#         try:
#             category = Category.objects.get(id=id_category)
#             category.delete()
#             return HttpResponse('Success!')
#         except: 
#             return
#     return

def attributes(request):
    return HttpResponse(serialize('json', Attribute.objects.filter(is_required=True)), content_type="application/json")

def attribute_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        code = request.POST.get('inputCode')
        label = request.POST.get('inputLabel')
        type_attr = request.POST.get('inputTypeAttr')
        is_required = request.POST.get('inputRequired')
        is_unique = request.POST.get('inputUnique')

        try:
            attribute = Attribute(
                code=code,
                lable=label,
                type_attr=type_attr,
                is_required=is_required,
                is_unique=is_unique,
            )
            attribute.save()
            return HttpResponse('Success!')
        except:
            return HttpResponse('Error!')
        
        return HttpResponse('Check')
    return HttpResponse('Error Add Attribute!')

def attribute_edit(request, id_attribute):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        try:
            code = request.POST.get('inputCode')
            label = request.POST.get('inputLabel')
            type_attr = request.POST.get('inputTypeAttr')
            is_required = request.POST.get('inputRequired')
            is_unique = request.POST.get('inputUnique')

            attribute = Attribute.objects.get(id=id_attribute)
            attribute.code = code
            attribute.label = label
            attribute.type_attr = type_attr
            attribute.is_required = is_required
            attribute.is_unique = is_unique

            attribute.save()
            return HttpResponse('Success!')
        except:
            return HttpResponse('Error!')
    return HttpResponse('Error Edit Attribute!')

def attribute_del(request, id_attribute):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':
        try:
            attribute = Attribute.objects.get(id=id_attribute)
            attribute.delete()
            return HttpResponse('Success!')
        except: 
            return
    return

####  _______________Product
####
####
####
####
####
####
####
####
####

@csrf_exempt
def upload_image(request):
    if check_rule(request) == 0:
        return HttpResponse(-3)
    if request.method == 'POST' and request.FILES['photo']:
        myfile = request.FILES['photo']
        validate_image = ['image/png', 'image/jpg', 'image/jpeg', 'image/gif']
        print(myfile.size)
        if myfile.size > 2000000:
            return HttpResponse(-2)

        if myfile.content_type in validate_image:
            fs = FileSystemStorage(location=settings.BASE_DIR + '/media/product')
            filename = fs.save(myfile.name, myfile)
            image = Image(
                image_link=filename,
                user_id=Account.objects.get(pk=request.session.get('user')['id']),
            )
            image.save()
            return HttpResponse(image.id)
        else:
            return HttpResponse(0)
    return HttpResponse(-1)
        
@csrf_exempt
def del_image(request, id_image):
    if request.method == 'DELETE':
        image = Image.objects.get(pk=int(id_image))
        path = settings.BASE_DIR + '/media/product' + image.image_link.url
        if os.path.exists(path):
            os.remove(path)
            image.delete()
            return HttpResponse('Xoa thanh cong')
        
@csrf_exempt   
def product_add(request):
    if request.method == "POST":
        count_product = request.POST.get('inputCountProduct')
        if int(count_product) < 1:
            return HttpResponse('KHong the tao moi san pham')

        code = request.POST.get('inputCode')
        name = request.POST.get('inputName')
        detail = request.POST.get('inputDetail')
        price_origin = request.POST.get('inputPrice')
        origin = request.POST.get('inputOrigin')
        account_created = Account.objects.get(pk=request.session.get('user')['id'])
        product_config = Product(
            code=code,
            name= name,
            detail=detail,
            origin=origin,
            type_product=True,
            price=price_origin,
            archive=False,
            account_created=account_created,
        )
        product_config.save()

        count_category = request.POST.get('inputCountCategory')
        for i in range(int(count_category)):
            id = request.POST.get('inputCategory['+ str(i) +']')
            product_category = Product_Category(
                product_id = product_config,
                category_id = Category.objects.get(pk=int(id))
            )
            product_category.save()

        count_images = request.POST.get('inputCountImage') #edit input
        for i in range(int(count_images)):
            id = request.POST.get('inputImage['+ str(i) +']')
            image = Product_Image(
                product_id = product_config,
                image_id = Image.objects.get(pk=int(id))
            )
            image.save()

        v = 1
        for i in range(int(count_product)):
            if count_product != 1:
                code_type = code + ' .v' + str(v)
            else: 
                code_type = code
            product = Product(
                code=code_type,
                name=name,
                detail=detail,
                origin=origin,
                price=request.POST.get('inputVersion['+ str(i) +'][price]'),
                type_product=False,
                archive=False,
                account_created=account_created,
            )
            product.save()
            
            Link_Type.objects.create(product_id=product, parent_product=product_config.id)

            data = request.POST.get('inputVersion['+ str(i) +'][value]')
            list_attr = data.split(' | ')
            attr = Attribute.objects.filter(is_required=True)
            index = 0
            for item in list_attr:
                product_attr = Product_Attribute(
                    product_id=product,
                    attribute_id=attr[index],
                    value=item,
                )
                product_attr.save()
                index = index + 1 

            v = v + 1
            # percent = request.POST.get('inputAttribute') #edit input
            # date_start = request.POST.get('inputAttribute')  #edit input
            # date_end = request.POST.get('inputAttribute')  #edit input
            # discount = Discount(
            #     product_id=product.id,
            #     percent=percent,
            #     date_start=date_start,
            #     date_end=date_end,
            # )

        return HttpResponse(1)



@csrf_exempt
def product(request, id_product):
    if request.method == 'GET':
        product_detail = dict()
        product_config = Product.objects.filter(id=int(id_product), type_product=True)
        if product_config.count() == 0:
            return HttpResponse(-1)

        product_detail['name'] = product_config[0].name
        product_detail['detail'] = product_config[0].detail
        product_detail['origin'] = product_config[0].origin
        product_detail['code'] = product_config[0].code
        product_detail['price_origin'] = product_config[0].price

        product_category = Product_Category.objects.filter(product_id=int(id_product), archive=False)
        list_category  = []
        for item in product_category:
            category_dict = dict()
            category = Category.objects.get(pk=item.category_id.id)
            category_dict['id'] = category.id
            category_dict['name_category'] = category.name_category
            category_dict['quantity'] = category.quantity
            list_category.append(category_dict)
        product_detail['list_category'] = list_category

        product_image = Product_Image.objects.filter(product_id=int(id_product), archive=False).order_by('image_id_id')
        list_image = []
        for item in product_image:
            image_dict = dict()
            image = Image.objects.get(pk=item.image_id.id)
            image_dict['id']  = image.id
            image_dict['image_link'] =  '/product' + image.image_link.url
            image_dict['is_default'] = image.is_default
            image_dict['user_id'] = image.user_id.id
            list_image.append(image_dict)
        product_detail['list_image'] = list_image

        #lay ra danh sach phien ban
        link_type = Link_Type.objects.filter(parent_product=product_config[0].id, product_id__archive=False)
        list_attr = []
        list_price = []
        for item in link_type:
            list_tmp = []
            list_price.append(item.product_id.price)
            product_attr = Product_Attribute.objects.filter(product_id=item.product_id.id, archive=False).order_by('attribute_id')
            for item in product_attr:
                list_tmp.append(item.value)
            list_attr.append(list_tmp)
    
        #su dung matrix de tra ve danh sach gia tri cho tung thuoc tinh
        len_atr = len(list_attr[0])
        len_verison = len(list_attr)
        list_value_attr = []
        for i in range(len_atr):
            list_temp = []
            for j in range(len_verison):
                if list_attr[j][i] not in list_temp:
                    list_temp.append(list_attr[j][i])
            list_value_attr.append(list_temp)

        product_detail['list_attr'] = list_value_attr
        product_detail['list_price'] = list_price

        return  HttpResponse(json.dumps(product_detail), content_type="application/json")

    if request.method == 'POST':
        if Product.objects.filter(pk=id_product).exists() == True:
            now = timezone.now()
            product = Product.objects.get(pk=id_product)
            product_link = Link_Type.objects.filter(parent_product=product.id, product_id__archive=False).values_list('product_id_id')
            Product.objects.filter(pk__in=product_link).update(archive=True, archive_at=now)
            Product_Category.objects.filter(product_id_id=product.id, archive=False).update(archive=True, archive_at=now)
            Product_Image.objects.filter(product_id_id=product.id, archive=False).update(archive=True, archive_at=now)
            Product_Attribute.objects.filter(product_id_id__in=product_link, archive=False).update(archive=True, archive_at=now)

            
            #request 
            code = request.POST.get('inputCode')
            name = request.POST.get('inputName')
            detail = request.POST.get('inputDetail')
            price_origin = request.POST.get('inputPrice')
            origin = request.POST.get('inputOrigin')
            account_created = Account.objects.get(pk=request.session.get('user')['id'])
            
            # Edit product origin
            product.code=code
            product.name= name
            product.detail=detail
            product.origin=origin
            product.price=price_origin
            product.save()

            count_category = request.POST.get('inputCountCategory')
            for i in range(int(count_category)):
                id_category = request.POST.get('inputCategory['+ str(i) +']')
                product_category = Product_Category(
                    product_id = product,
                    category_id = Category.objects.get(pk=int(id_category))
                )
                product_category.save()

            count_images = request.POST.get('inputCountImage') #edit input
            for i in range(int(count_images)):
                id_image = request.POST.get('inputImage['+ str(i) +']')
                image = Product_Image(
                    product_id = product,
                    image_id = Image.objects.get(pk=int(id_image))
                )
                image.save()

            count_product = request.POST.get('inputCountProduct')
            if int(count_product) < 1:
                return HttpResponse(-1)
            v = 1
            for i in range(int(count_product)):
                if count_product != 1:
                    code_type = code + ' .v' + str(v)
                else: 
                    code_type = code
                product2 = Product(
                    code=code_type,
                    name=name,
                    detail=detail,
                    origin=origin,
                    price=request.POST.get('inputVersion['+ str(i) +'][price]'),
                    type_product=False,
                    archive=False,
                    account_created=account_created,
                )
                product2.save()
                
                Link_Type.objects.create(product_id=product2, parent_product=product.id)

                data = request.POST.get('inputVersion['+ str(i) +'][value]')
                list_attr = data.split(' | ')
                attr = Attribute.objects.filter(is_required=True)
                index = 0
                for item in list_attr:
                    product_attr = Product_Attribute(
                        product_id=product2,
                        attribute_id=attr[index],
                        value=item,
                    )
                    product_attr.save()
                    index = index + 1 
                v = v + 1
                # percent = request.POST.get('inputAttribute') #edit input
                # date_start = request.POST.get('inputAttribute')  #edit input
                # date_end = request.POST.get('inputAttribute')  #edit input
                # discount = Discount(
                #     product_id=product.id,
                #     percent=percent,
                #     date_start=date_start,
                #     date_end=date_end,
                # )
            return HttpResponse(1)

    if request.method == 'DELETE':
        # kiem tra san pham da duoc dang chua?
        # cau huy goi tin de duoc xoa
        return

def products(request):
    if request.method == 'GET':
        if request.GET.get('table') == 'true':
            products = []
            prod_all = Product.objects.filter(type_product=True, archive=False).order_by('-pk')
            for item in prod_all:
                if Link_Type.objects.filter(parent_product=item.id).exists() == True:
                    product = []
                    product.append('<a href="/merchant/product/edit/'+ str(item.id) +'">SP'+ str(item.id) +'</a>')
                    product.append(item.name)
                    product.append(str(item.price) + ' VND')
                    image = Product_Image.objects.filter(product_id_id=item.id).order_by('image_id_id').first()
                    if Product_Image.objects.filter(product_id_id=item.id).exists() == True:
                        product.append('<div class="tbl_thumb_product"><img src="/product' + image.image_id.image_link.url + '" /></div>')
                    else:
                        product.append('<div class="tbl_thumb_product"><img src="/static/website/images/product_1.jpg" /></div>')
                    if item.consider == 1:
                        product.append('<p style="color:green">Được chấp thuận</p>')
                    if item.consider == 0:
                        product.append('<p style="color:red">Bị khóa</p>')
                    if item.consider == 2:
                        product.append('<p style="color:blue">Đang xem xét</p>')
                    products.append(product)
            return HttpResponse(json.dumps(products), content_type="application/json")
        if request.GET.get('posted') == 'false':
            if 'include' in request.GET: 
                # http://localhost:8000/merchant/products?posted=false&include=id_product
                # lay danh sach san chua dang san pham do
                list_id = Post_Product.objects.values_list('product_id__id').filter(is_activity=True, is_lock=False).exclude(product_id__id=request.GET.get('include'))
                return HttpResponse(serialize('json', Product.objects.exclude(pk__in=list_id).filter(type_product=True)), content_type="application/json")
            list_id = Post_Product.objects.values_list('product_id__id').filter(is_activity=True, is_lock=False)
            return HttpResponse(serialize('json', Product.objects.exclude(pk__in=list_id).filter(type_product=True)), content_type="application/json")
        return HttpResponse(0)
    return HttpResponse(0)


### ----------------------Service
###
###
###
###
###
###
###
###
###

def services(request):
    return HttpResponse(serialize('json', Service.objects.filter(is_active=True)), content_type="application/json")


def service(request, id_service):
    # if check_rule(request) == 0:
    #     return HttpResponse('Error')
    if request.method == "GET":
        return HttpResponse(serialize('json', Service.objects.filter(pk=id_service)), content_type="application/json")


@csrf_exempt        
def purchase_service(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')
    if request.method == 'POST':
        purchase_name = request.POST.get('inputPurchaseName')
        merchant_id = Account.objects.get(pk=request.session.get('user')['id'])
        service_id = request.POST.get('inputServiceId')
        amount = request.POST.get('inputAmount')
        state = request.POST.get('inputState')

        try:
            service = Service.objects.get(pk=service_id)
            purchase_service = Purchase_Service(
                purchase_name=purchase_name,
                merchant_id=merchant_id,
                service_id=service,
                amount=amount,
                state=int(state),
            )
            purchase_service.save()

            account_service = Account_Service.objects.filter(account__id=merchant_id.id, service__id=service.id)
            if account_service.count() == 1:
                remain = account_service[0].remain
                account_service.update(remain=remain+service.value)
                return HttpResponse('Success!')
            return HttpResponse('Error!')
        except:
            return HttpResponse('Error!')
    return HttpResponse('Error Add Purchase!')


### -------  Post Product
###
###
###
###
###
###
###
###
###



@csrf_exempt 
def post_add(request):
    if check_rule(request) == 0:
        return HttpResponse('Error')

    if request.method == 'POST':

        product_id = request.POST.get('inputProduct')
        service_id = request.POST.get('inputService')
        creator_id = Account.objects.get(pk=request.session.get('user')['id'])

        # check  product 
        if Post_Product.objects.filter(product_id__id=product_id, is_activity=True, is_lock=False).exists():
            return HttpResponse('Error! This product was used in the Post other!')
        # check remain post
        if Account_Service.objects.filter(service_id=int(service_id), account_id=creator_id, remain__gt=0).exists == False:
            return HttpResponse('Loi! Ban khong co du goi tin do')

        service = Service.objects.get(pk=int(service_id))
        quantity = request.POST.get('inputQuantity')


        if int(quantity) > service.quantity_product:
            return HttpResponse('So luong san pham khong duoc lon hon '+ str(service.value))
        if int(quantity) <= 0 or quantity == '':
            return HttpResponse('So luong san pham phai lon hon 0')

    
        post_product = Post_Product(
            product_id = Product.objects.get(pk=product_id),
            post_type = service,
            creator_id = creator_id,
            quantity = int(quantity),
            visable_vip = service.visable_vip,
            expire = datetime.now() + timedelta(days=service.day_limit),
        )
        post_product.save()
        account_service = Account_Service.objects.filter(account_id=creator_id, service_id=post_product.post_type_id)
        if account_service.count() == 1:        
            remain = account_service[0].remain
            account_service.update(remain=remain-1)
            return HttpResponse('Success')
        return HttpResponse('Error Account servive sub remain')

    return HttpResponse('Error')


def check_expire_post(id_post):
    post = Post_Product.objects.get(pk=id_post)
    if post.expire.replace(tzinfo=None) <= datetime.now():
        post.update(is_lock=True, is_activity=False)


@csrf_exempt 
def post(request, id_post):
    if request.method == 'GET':
        return HttpResponse(serialize('json', Post_Product.objects.filter(pk=id_post)), content_type="application/json")

    if request.method == 'POST':

        #check an update expire post  \

        # kiem tra tin dang co ton tai khong?
        if Post_Product.objects.filter(pk=id_post).exists() == False:
            return HttpResponse('Tin dang khong ton tai!')

        post = Post_Product.objects.get(pk=id_post)
        # kiem tra da het  hang cua
        if post.is_lock == True:
            return HttpResponse('Tin dang da het hang, Khong duoc phep sua!')

        quantity = request.POST.get('inputQuantity')

        if int(quantity) > (post.post_type.quantity_product - post.bought):
            return HttpResponse('So luong san pham khong duoc lon hon {}'.format(str(post.quantity - post.bought)))
        if int(quantity) <= 0 or quantity == '':
            return HttpResponse('So luong san pham phai lon hon 0')

        post.quantity = quantity
        post.is_activity = request.POST.get('inputIsActivity')
        post.save()
        return HttpResponse('Thuc hien thanh cong!')

    if request.method == 'DELETE':
        if Post_Product.objects.filter(pk=id_post).exists() == False and Post_Product.objects.filter(pk=id_post).count == 1:
            return HttpResponse('Tin dang khong ton tai!')
        post = Post_Product.objects.get(pk=id_post)
        if post.is_lock == True:
            return HttpResponse('Tin dang da het han!')
        if post.is_activity == False:
            return HttpResponse('Thuc hien that bai!\nTin dang da tat hien thi ')
        post.is_activity = False
        post.save()
        return HttpResponse('Thuc hien thanh cong!\nTin dang da tat che do hien thi!')
    return
    
def posts(request):
    if request.method == 'GET':
        posts = []
        post_all = Post_Product.objects.filter(creator_id__id=request.session.get('user')['id'])
        for item in post_all:
            post = []
            post.append('<a href="/merchant/post/edit/'+ str(item.id) +'"> TD'+ str(item.id) +'</a>')
            post.append('<a href="/merchant/product/edit/'+ str(item.product_id_id) +'"> SP'+ str(item.product_id_id) +'</a>')
            post.append('15')
            post.append(item.expire.replace(tzinfo=None).strftime("%d/%m/%Y %H:%M"))
            post.append(item.post_type.service_name)
            posts.append(post)
        return HttpResponse(json.dumps(posts), content_type="application/json")