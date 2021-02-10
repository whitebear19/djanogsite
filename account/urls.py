from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'account'
urlpatterns = [   
    path('login',view=views.login_custom, name='login'),
    path('register',view=views.register_custom, name='register'),
   
    path('home',view=views.home, name='home'),
    path('profile',view=views.profile, name='profile'),
    path('check_register',view=views.check_register, name='check_register'),
    path('check_login',view=views.check_login, name='check_login'),
  
    path('',view=views.index, name='index'),
    path('logout',view=views.logout, name='logout'),
    path('messages',view=views.messages, name='messages'),  
    path('close_account',view=views.close_account, name='close_account'),
    
    # ajax
    path('upload_avatar',view=views.upload_avatar, name='upload_avatar'), 
    path('store_basicinfo',view=views.store_basicinfo, name='store_basicinfo'),
]