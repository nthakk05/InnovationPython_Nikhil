from django.urls import path, include

from . import views

urlpatterns = [

    path('a', views.Congratulations, name='Thanks'),
    path('login', views.save_form, name='save_form'),
    path('', views.Home, name = 'Home' ),
]
