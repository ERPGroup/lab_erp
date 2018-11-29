from django.urls import path

from . import views, functions

### READ ME ###
## Url chia lam 2 thanh phan function va view.
# view dung de hien thi bo khung giao dien html
# function de lay du lieu tu database sau do dan vao giao dien bang thong qua jquery (ajax)

urlpatterns = [
    # path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('',views.index,name='admin_index'),

    path('manager_users',views.users,name='manager_users'),
    path('manager_users_detail',views.users_add,name='add users'),
    path('user/see/<int:id_user>', views.user_info, name='user_info'),

    path('manager_services',views.services,name='Manager Services'),
    path('service/add', views.service_add, name='service_add'),
    path('service/edit/<int:id_service>', views.service_edit, name='service_edit'),
    
    path('manager_pay',views.payment,name="payment"),
    path('manager_payment_detail',views.payment_detail,name="payment_detail"),

    path('manager_posted',views.post,name="payment"),
    #path('manager_posted_detail',views.post_detail,name="payment"),
    path('post/edit/<int:id_post>', views.post_detail, name='post_edit'),

    path('manager_ads',views.ads,name="ads"),
    path('manager_ads_detail',views.ads_detail,name="ads"),

    path('manager_ads/register',views.ads_register,name="ads"),
    path('manager_ads/register_detail',views.ads_register_detail,name="ads"),

    path('manager_product',views.products,name="products"),
    path('manager_product_detail',views.products_detail,name="products"),
    path('product/see/<int:id_product>',views.product,name="see_product"),

    path('manager_category',views.categories,name="products"),
    path('category/add', views.category_add, name='category_add'),
    path('category/edit/<int:id_category>', views.category_edit, name='category_edit'),
    # PHUC: viet 2 url cua add va edit category sao comment nay
    # chu y function la "views.<ten function>""
    path('manager_category_detail',views.category_detail,name="products"),
   



    #tuong tu viet cac url cua attribute giong category ben duoi comment nay
    path('manager_attribute',views.attributes,name="attribute"),
    path('manager_attribute_detail',views.manager_attribute_detail,name="products"),
    path('attribute/add', views.attribute_add, name='attribute_add'),
    path('attribute/edit/<int:id_attribute>', views.attribute_edit, name='attribute_edit'),


    path('statistical',views.statistical,name="statistical"),



    #function

    path('services', functions.services, name='services'),
    path('service', functions.service_add, name="service_add"),
    path('service/<int:id_service>', functions.service, name="service"),
    
    # Phuc tham khao url Serive o tren va viet url Category va Attribute ben duoi comment

    path('categories',functions.categories, name='categories'),
    path('category',functions.category_add, name="category_add"),
    path('category/<int:id_category>',functions.category, name="category"),

    path('attributes',functions.attributes, name='attributes'),
    path('attribute',functions.attribute_add, name="attribute_add"),
    path('attribute/<int:id_attribute>',functions.attribute, name="attribute"),

    # product
    path('products', functions.products, name='products'),
    path('product/<int:id_product>', functions.product, name='product'),

    #post
    path('posts',functions.posts, name='posts'),

    #account service
     path('account_services', functions.account_services, name='account_services'),

    #user
    path('user/<int:id_user>', functions.user, name='user')


   # path(r'^ajax/update_ads/$', views.update_ads, name='Update Ads'),
]