from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'data'
urlpatterns = [   
      
    path('dashboard',view=views.dashboard, name='dashboard'),
    path('insert',view=views.insert, name='insert'),
   
    # ajax
    path('store',view=views.store, name='store'),
    path('store_delivery',view=views.store_delivery, name='store_delivery'),
    
    path('get_data',view=views.get_data, name='get_data'),
    path('get_delivery',view=views.get_delivery, name='get_delivery'),
    
]