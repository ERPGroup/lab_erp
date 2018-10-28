from django.urls import path

from . import views

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
]