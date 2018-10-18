from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/',views.login,name='login'),
   path('manager_product',views.product,name='product'),
   path('manager_product_detail',views.product_detail,name='product'),
   path('manager_post',views.posted,name='product'),
   path('manager_post_detail',views.posted_detail,name='product'),
   path('manager_warehose',views.warehose,name='warehose'),
   path('order',views.order,name='order'),
   path('order_detail',views.order_detail,name='order'),
   path('statistial_post',views.statistical_post,name='statis'),
   path('service_post',views.service_post,name='servies'),
   path('service_ads',views.service_ads,name='servies'),
]