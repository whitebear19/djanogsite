from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'contract'
urlpatterns = [   
      
    path('dashboard',view=views.dashboard, name='dashboard'),
    path('insert',view=views.insert, name='insert'),
    
    # ajax

    path('store',view=views.store, name='store'),
    path('accept',view=views.accept, name='accept'),
    path('get_transport',view=views.get_transport, name='get_transport'),
    path('get_contract',view=views.get_contract, name='get_contract'),
    path('get_contract_user',view=views.get_contract_user, name='get_contract_user'),
    
]