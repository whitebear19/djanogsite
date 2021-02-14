from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import math
import requests
import time
import datetime
import json
import os 
import random
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy



from account.models import CustomUser

from .models import Data
import datetime
from datetime import timedelta
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from PIL import Image
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags


def dashboard(request):
    
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('/login')
       
    
    return render(request,'data/dashboard.html',{}) 

def insert(request):
    
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('/login')
       
    
    return render(request,'data/insert.html',{}) 

# ajax

def store(request):
               
    name = request.POST.get('name')
    volume = request.POST.get('volume')
    available = request.POST.get('available')
    try:
        user = request.user
        row = Data(name=name,volume=volume,available=available,user_id=user.id)
        row.save()
        return JsonResponse({'response':True})
    except:
        return JsonResponse({'response':False})

def get_data(request):

    results = []      

    try:
        datatemp = Data.objects.all()
        for item in datatemp:
            data = {}
            data['name'] = item.name
            data['volume'] = item.volume
            data['available'] = item.available
            results.append(data)
        return JsonResponse({'response':results})
    except:
        return JsonResponse({'response':results})
