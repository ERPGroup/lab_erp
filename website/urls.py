from django.urls import path

from . import views, functions, cart

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login-website'),
    path('logout',views.logout, name='logout-website'),
    path('register', views.register, name='register'),
    path('index',views.index,name="index"),
    path('activity/<email>/<code>/', views.activity_account, name='activity_account'),
    path('request_new_password/<email>/<code>/', views.request_new_password, name='request_new_password'),
    path('activity_merchant/<email>/<code>/', views.activity_merchant, name='activity_merchant'),
    path('activity_ad/<email>/<code>/', views.activity_ad, name='activity_ad'),
    #path('forgot_password/', views.forgot_password, name='forgot_password'),
    #path('request_merchant/', views.request_merchant, name='request_merchant'),

    path('shop/<int:id_shop>', views.shop, name='shop'),
    path('search', views.search, name='search'),

    
    path('collections/<int:id_category>', views.collections, name='collections'),
    path('post/<int:id_post>', views.detail_post, name='detail_post'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),


    #function

    path('forgot_password', functions.forgot_password, name='forgot_password'),
    path('categorys', functions.categorys, name='categorys'),

    path('get_profile_payment', functions.get_profile_payment, name='get_profile_payment'),
    path('product_by_category/<int:id_category>', functions.product_by_category, name='product_by_category'),
    path('get_avatar_product/<int:id_product>', functions.get_avatar_product, name='get_avatar_product' ),
    path('payment', functions.payment, name='payment'),

    path('data', functions.get_data, name='data'),

    path('product_collection/<int:id_category>', functions.product_collection, name='product_collection'),

    path('product_data/<int:id_product>', functions.product, name='product'),

    path('post_data/<int:id_post>', functions.post, name='post'),
    path('get_data_hot_buy', functions.get_data_hot_buy, name="get_data_hot_buy"),
    path('get_data_related/<int:id_category>', functions.get_data_related, name="get_data_related"),

    path('f_register', functions.register, name='f_register'),
    path('f_search', functions.search, name='f_search'),
    path('rating_merchant/<int:id_post>', functions.rating_merchant, name='rating_merchant'),
    path('rating_merchant_shop/<int:id_shop>', functions.rating_merchant_shop, name='rating_merchant_shop'),
    path('get_product_shop/<int:id_shop>', functions.get_product_shop, name='get_product_shop'),
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
    path('getAds',functions.getAds,name="get_ads_top"),

    path('product',views.product,name="product"),

]