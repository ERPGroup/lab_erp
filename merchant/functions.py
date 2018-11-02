from django.shortcuts import render, redirect
from admin import views
# Create your views here.

from django.http import HttpResponse, Http404
from website.models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.files.storage import FileSystemStorage, Storage


def categorys(request):
    return HttpResponse(serialize('json', Category.objects.all()))

def category(request, id_category):
    if request.method == "GET":
        return HttpResponse(serialize('json', Category.objects.filter(pk=id_category)))

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
        validate_image = ['image/png', 'image/jpg']
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
            return HttpResponse('do khong hai hinh anh', status=200)
        
@csrf_exempt
def del_image(request, id_image):
    if request.method == 'POST':
        image = Image.objects.get(pk=id_image)
        image.delete()
        Storage.delete()
        
