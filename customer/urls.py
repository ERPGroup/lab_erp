from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('profile',views.profile,name='profile'),
    path('history_order/',views.history_order,name='history_order'),
    path('order_detail',views.history_order_detail,name='order_detail'),


    #function 
    

]