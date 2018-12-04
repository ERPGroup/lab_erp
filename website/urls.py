from django.urls import path

from . import views, functions, cart

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login-website'),
    path('logout/',views.logout, name='logout-website'),
    path('register/', views.register, name='register'),
    path('index',views.index,name="index"),
    path('activity/<email>/<code>/', views.activity_account, name='activity_account'),
    path('request_new_password/', views.request_new_password, name='request_new_password'),
    path('request_merchant/', views.request_merchant, name='request_merchant'),
    path('activity_merchant/<email>/<code>/', views.activity_merchant, name='activity_merchant'),


    
    path('collections/<int:id_category>', views.collections, name='collections'),
    path('product/<int:id_product>', views.detail_product, name='detail_product'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),


    #function
    path('product_by_category/<int:id_category>', functions.product_by_category, name='product_by_category'),
    path('get_avatar_product/<int:id_product>', functions.get_avatar_product, name='get_avatar_product' ),
    path('payment', functions.payment, name='payment'),

    path('data', functions.get_data, name='data'),


    #cart
    path('add/<int:id_product>', cart.add, name='add'),
    path('sub/<int:id_product>', cart.sub, name='sub'),
    path('remove/<int:id_product>', cart.remove, name='remove'),
    path('clear', cart.clear, name='clear'),
    path('show', cart.show, name='show'),
    
    #Ly Thanh
    path('getAds',functions.getAds,name="get_ads_top")

]