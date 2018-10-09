from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('',views.index,name='admin_index'),
    path('manager_users',views.users,name='manager_users'),
]