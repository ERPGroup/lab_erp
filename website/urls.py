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
    path('post/<int:id_post>', views.detail_post, name='detail_post'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),


    #function

    path('get_profile_payment', functions.get_profile_payment, name='get_profile_payment'),
    path('product_by_category/<int:id_category>', functions.product_by_category, name='product_by_category'),
    path('get_avatar_product/<int:id_product>', functions.get_avatar_product, name='get_avatar_product' ),
    path('payment', functions.payment, name='payment'),

    path('data', functions.get_data, name='data'),

    path('product_collection/<int:id_category>', functions.product_collection, name='product_collection'),

    path('product_data/<int:id_product>', functions.product, name='product'),

    path('post_data/<int:id_post>', functions.post, name='post'),
    path('get_data_hot_buy', functions.get_data_hot_buy, name="get_data_hot_buy"),
    path('get_data_related/<int:id_post>', functions.get_data_related, name="get_data_related"),

    #cart
    path('add/<int:id_product>', cart.add, name='add'),
    path('add_qty/<int:id_product>/<int:qty>', cart.add_qty, name='add_qty'),
    path('sub/<int:id_product>', cart.sub, name='sub'),
    path('set_qty/<int:id_product>/<int:qty>', cart.set_qty, name='set_qty'),
    path('remove/<int:id_product>', cart.remove, name='remove'),
    path('clear', cart.clear, name='clear'),
    path('show', cart.show, name='show'),
    path('count', cart.count, name='count'),
    
    #Ly Thanh
    path('getAds',functions.getAds,name="get_ads_top")

]