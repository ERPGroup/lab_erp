from django.urls import path

from . import views
from . import functions

### READ ME ###
## Url chia lam 2 thanh phan function va view.
# view dung de hien thi bo khung giao dien html
# function de lay du lieu tu database sau do dan vao giao dien bang thong qua jquery (ajax)

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),


    path('manager_product',views.product,name='manager product'),
    path('product/add', views.product_add, name='product_add'),
    path('product/edit/<int:id_product>', views.product_edit, name='product_edit'),
    path('manager_product_detail',views.product_detail,name='product'),



    path('manager_post',views.posted,name='product'),
    path('post/add', views.post_add, name='post_add'),
    path('post/edit/<int:id_post>', views.post_edit, name='post_edit'),
    path('manager_post_detail',views.posted_detail,name='product'),

    path('manager_warehose',views.warehose,name='warehose'),

    path('order',views.order,name='order'),
    path('order_detail',views.order_detail,name='order'),

    path('statistial_post',views.statistical_post,name='statis'),

    path('service_post',views.service_post,name='servies'),
    path('purchase_service/<int:id_service>', views.purchase_service, name='purchase_service'),





    #function urls
    path('categorys', functions.categorys, name='categorys'),
    path('category/<int:id_category>', functions.category, name='category'),
    path('category', functions.category_add, name='category_add'),

    path('upload_image', functions.upload_image, name='upload_image'),
    path('delete_image/<int:id_image>', functions.del_image, name='delete_image'),

    path('attributes', functions.attributes, name='attributes'),

    path('product', functions.product_add, name='product_add'),
    path('product/<int:id_product>', functions.product, name='product'),
    path('products', functions.products, name='products'),

    path('services', functions.services, name='services'),
    path('service/<int:id_service>', functions.service, name='service'),
    path('purchase_service', functions.purchase_service, name='fun_purchase_service'),
    

    path('account_services', functions.account_services, name='account_services'),


    path('posts', functions.posts, name='posts'),
    path('post', functions.post_add, name='post_add'),
    path('post/<int:id_post>', functions.post, name='post'),

    ### Ly Thanh 
    path('getListAds/',functions.get_my_choices_2,name="remove"),
    path('getDateAvailable/<position>&<int:id_ads>',functions.getDateAvailable,name="get_avail"),
    path('post_ads/',views.post_ads,name="ads"),
    path('upload_image_ads', functions.upload_image_ads, name='upload_image'),
    path('delete_image_ads/<int:id_image>', functions.del_image_ads, name='delete_image'),
    path('purchase_service_ads', functions.purchase_service_ads, name='fun_purchase_service'),
    path('upload_ads/',functions.post_ads,name="post_ads"),
    path('post_ads_2/',functions.post_ads_2,name="post_ads"),
    path('ads_register/<int:id_ads>',views.service_ads_register, name='ads'),
    path('service_ads',views.service_ads,name='servies'),

    ###
]