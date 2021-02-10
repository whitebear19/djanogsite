
from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'chat'
urlpatterns = [   
    path('get_all_room',view=views.get_all_room, name='get_all_room'),      
    path('get_new_message_global',view=views.get_new_message_global, name='get_new_message_global'),  
    path('get_new_message',view=views.get_new_message, name='get_new_message'),  
    path('set_read',view=views.set_read, name='set_read'),
    path('store_message',view=views.store_message, name='store_message'),
    path('request_chat',view=views.request_chat, name='request_chat'),    
    path('get_stored_message',view=views.get_stored_message, name='get_stored_message'),
    path('get_stored_message_nav',view=views.get_stored_message_nav, name='get_stored_message_nav'),
    path('clear_message_alert',view=views.clear_message_alert, name='clear_message_alert'),    
    path('clear_noti_alert',view=views.clear_noti_alert, name='clear_noti_alert'),    
    
]