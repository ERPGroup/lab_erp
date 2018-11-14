from django.urls import path

from . import views
from . import functions

urlpatterns = [
   path('', views.index, name='index'),
   path('login/',views.login,name='login'),
   path('manager_product',views.product,name='product'),
   path('product/add', views.product_add, name='product_add'),
   path('product/edit/<int:id_product>', views.product_edit, name='product_edit'),
   path('manager_product_detail',views.product_detail,name='product'),
   path('manager_post',views.posted,name='product'),
   path('manager_post_detail',views.posted_detail,name='product'),
   path('manager_warehose',views.warehose,name='warehose'),
   path('order',views.order,name='order'),
   path('order_detail',views.order_detail,name='order'),
   path('statistial_post',views.statistical_post,name='statis'),
   path('service_post',views.service_post,name='servies'),
   path('service_ads',views.service_ads,name='servies'),
   path('ads_register',views.service_ads_register, name='ads'),

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


   path('services', functions.services, name='services'),
   path('service/<int:id_service>', functions.service, name='service'),
   path('purchase_service', functions.purchase_service, name='fun_purchase_service'),


]