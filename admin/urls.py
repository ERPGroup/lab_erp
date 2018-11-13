from django.urls import path

from . import views, functions

urlpatterns = [
    # path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('',views.index,name='admin_index'),
    path('manager_users',views.users,name='manager_users'),
    path('manager_users_detail',views.users_add,name='add users'),
    path('manager_servies',views.servies,name='Manager Servies'),
    path('service/add',views.servies_add,name='add servies'),
    path('manager_pay',views.payment,name="payment"),
    path('manager_payment_detail',views.payment_detail,name="payment_detail"),
    path('manager_posted',views.post,name="payment"),
    path('manager_posted_detail',views.post_detail,name="payment"),
    path('manager_ads',views.ads,name="ads"),
    path('manager_ads_detail',views.ads_detail,name="ads"),
    path('manager_ads/register',views.ads_register,name="ads"),
    path('manager_ads/register_detail',views.ads_register_detail,name="ads"),
    path('manager_product',views.products,name="products"),
    path('manager_product_detail',views.products_detail,name="products"),
    path('manager_category',views.categories,name="products"),
    path('manager_category_detail',views.category_detail,name="products"),
    path('statistical',views.statistical,name="statistical"),



    #function
    path('service', functions.service_add, name="service_add"),
    path('manager_attribute',views.manager_attribute,name="attribute"),
    path('manager_attribute_detail',views.manager_attribute_detail,name="products"),

   # path(r'^ajax/update_ads/$', views.update_ads, name='Update Ads'),
]