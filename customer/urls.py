from django.urls import path

from . import views, functions

urlpatterns = [
    # path('', views.index, name='index'),
    path('profile',views.profile,name='profile'),
    path('history_order',views.history_order,name='history_order'),
    path('bill_detail/<int:id_order>',views.bill_detail,name='bill_detail'),
    # path('print_bill/<int:id_order>',views.print_bill,name='print_bill'),
    # path('print_bill/data.js', views.data, name='data'),

    #function 
    path('user',functions.profile,name='user'),
    path('password',functions.change_pw,name='password'),
    path('info',functions.change_info,name='info'),
    path('success_order/<int:id_order>', functions.success_order, name='success_order'),
    path('cancel_order/<int:id_order>', functions.cancel_order, name='cancel_order'),
    path('cancel_order_item/<int:id_order_item>', functions.cancel_order_item, name='cancel_order_item'),
    #path('print_bill', functions.print_bill, name='print_bill'),
    #path('get_orders', functions.get_orders, name='get_orders'),

]