from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.signup_view,name='signup'),
    path('login', views.login_view, name='login'),
    path('home', views.home_view, name='home'),
    path('logout',views.logout_view,name='logout')

]
