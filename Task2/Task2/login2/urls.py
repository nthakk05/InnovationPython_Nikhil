from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('login2', views.user_login, name='login'),
    path('success', views.index, name = 'index'),
    path('AboutUs', views.AboutUs, name = 'AboutUs'),
    path('logout',views.logout, name='logout'),

]