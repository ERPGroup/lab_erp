from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/',views.login,name='login'),
   path('manager_product',views.product,name='product'),
   path('manager_product_detail',views.product_detail,name='product'),
]