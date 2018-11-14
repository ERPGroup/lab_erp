from django.shortcuts import render, redirect
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404, JsonResponse
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.files.storage import FileSystemStorage, Storage

import json

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

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['photo']:
        myfile = request.FILES['photo']
        validate_image = ['image/png', 'image/jpg', 'image/jpeg', 'image/gif']
        print(myfile.size)
        if myfile.size > 1000000:
            return HttpResponse(-2)

        if myfile.content_type in validate_image:
            fs = FileSystemStorage(location=settings.BASE_DIR + '/media/product')
            filename = fs.save(myfile.name, myfile)
            image = Image(
                image_link=myfile.name,
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
        if Storage.exists(name=path):
            Storage.delete(path)
            image.delete()
        return HttpResponse('1')
        
@csrf_exempt   
def product_add(request):
    if request.method == "POST":
        print(request.POST)
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
            is_visible=True,
            is_activity=True,
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

        count_product = request.POST.get('inputCountProduct')
        for i in range(int(count_product)):
            product = Product(
                code=code,
                name=name,
                detail=detail,
                origin=origin,
                price=request.POST.get('inputVersion['+ str(i) +'][price]'),
                type_product=False,
                is_visible=True,
                is_activity=True,
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

        product_category = Product_Category.objects.filter(product_id=int(id_product))
        list_category  = []
        for item in product_category:
            category_dict = dict()
            category = Category.objects.get(pk=item.category_id.id)
            category_dict['id'] = category.id
            category_dict['name_category'] = category.name_category
            category_dict['quantity'] = category.quantity
            list_category.append(category_dict)
        product_detail['list_category'] = list_category

        product_image = Product_Image.objects.filter(product_id=int(id_product)).order_by('image_id_id')
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
        link_type = Link_Type.objects.filter(parent_product=product_config[0].id)
        list_attr = []
        list_price = []
        for item in link_type:
            list_tmp = []
            list_price.append(item.product_id.price)
            product_attr = Product_Attribute.objects.filter(product_id=item.product_id.id).order_by('attribute_id')
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
        return

    if request.method == 'DELETE':
        return



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