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
            fs = FileSystemStorage(location=settings.BASE_DIR + '/media/merchant/product')
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
    if request.method == 'POST':
        image = Image.objects.get(pk=id_image)
        path = settings.BASE_DIR + '/media/merchant/product/' + image.image_link
        image.delete()
        if Storage.exists(path):
            Storage.delete(path)
        
@csrf_exempt   
def product_add(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('inputName')
        detail = request.POST.get('inputDetail')
        price_origin = request.POST.get('inputPrice')
        origin = request.POST.get('inputOrigin')
        account_created = Account.objects.get(pk=request.session.get('user')['id'])
        product_config = Product(
            name= name,
            detail=detail,
            origin=origin,
            type_product=True,
            is_visible=True,
            is_activity=True,
            archive=False,
            account_created=account_created,
        )
        product_config.save()

        list_category = request.POST.get('inputCategory[]')
        for item in list_category:
            product_category = Product_Category(
                product_id = product_config,
                category_id = Category.objects.get(pk=item)
            )
            product_category.save()

        list_images = request.POST.get('inputImage[]') #edit input
        for item in list_images:
            image = Product_Image(
                product_id = product_config,
                image_id = Image.objects.get(pk=item)
            )
            image.save()

        count_product = request.POST.get('inputCountProduct')
        for i in range(int(count_product)):

            product = Product(
                name=name,
                detail=detail,
                origin=origin,
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

        product_iamge = Product_Image.objects.filter(product_id=int(id_product))
        list_image = []
        for item in product_iamge:
            image_dict = dict()
            image = Image.objects.get(pk=item.image_id.id)
            image_dict['id']  = image.id
            image_dict['image_link'] = settings.BASE_DIR + '/media/merchant/product' + image.image_link.url
            image_dict['is_default'] = image.is_default
            image_dict['user_id'] = image.user_id.id
            list_image.append(image_dict)
        product_detail['list_image'] = list_image

        #lay ra danh sach phien ban
        link_type = Link_Type.objects.filter(parent_product=product_config[0].id)

        list_atrr = []
        for item in link_type:
            list_tmp = []
            product_attr = Product_Attribute.objects.filter(product_id=item.product_id.id).order_by('attribute_id')
            for item in product_attr:
                list_tmp.append(item.value)
            list_atrr.append(list_tmp)

        #su dung matrix de tra ve danh sach gia tri cho tung thuoc tinh
        len_atr = len(list_atrr[0])
        len_verison = len(list_atrr)
        list_value_attr = []
        for i in range(len_atr):
            list_temp = []
            for j in range(len_verison):
                if list_atrr[j][i] not in list_temp:
                    list_temp.append(list_atrr[j][i])
            list_value_attr.append(list_temp)

        product_detail['list_atrr'] = list_value_attr

        return  HttpResponse(json.dumps(product_detail), content_type="application/json")