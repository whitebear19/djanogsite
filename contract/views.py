from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
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

from chat.models import Room,Message
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
from .models import Contract
from data.models import Data
def dashboard(request):
    
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('/login')
       
    
    return render(request,'contract/dashboard.html',{}) 

def insert(request):
    
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if user.verified == "0":
            return redirect('/confirm')
        else:            
            if user.professional != "1":
                return redirect('/contract/dashboard')
            else:
                return render(request,'contract/insert.html',{}) 

# ajax
def store(request):               
    name = request.POST.get('name')
    transport = request.POST.get('transport')
    d_address = request.POST.get('d_address')
    d_city = request.POST.get('d_city')
    d_zipcode = request.POST.get('d_zipcode')
    d_date = request.POST.get('d_date')
    e_address = request.POST.get('e_address')
    e_city = request.POST.get('e_city')
    e_zipcode = request.POST.get('e_zipcode')
    e_date = request.POST.get('e_date')
    i1_address = request.POST.get('i1_address')
    i1_city = request.POST.get('i1_city')
    i1_zipcode = request.POST.get('i1_zipcode')
    i1_date = request.POST.get('i1_date')
    i2_address = request.POST.get('i2_address')
    i2_city = request.POST.get('i2_city')
    i2_zipcode = request.POST.get('i2_zipcode')
    i2_date = request.POST.get('i2_date')
    try:
        user = request.user
        row = Contract(user_id=user.id,
                        c_num="",
                        transport=transport,
                        d_address=d_address,
                        d_city=d_city,
                        d_zipcode=d_zipcode,
                        d_date=d_date,
                        e_address=e_address,
                        e_city=e_city,
                        e_zipcode=e_zipcode,
                        e_date=e_date,
                        i1_address=i1_address,
                        i1_city=i1_city,
                        i1_zipcode=i1_zipcode,
                        i1_date=i1_date,
                        i2_address=i2_address,
                        i2_city=i2_city,
                        i2_zipcode=i2_zipcode,
                        i2_date=i2_date
                        )
        row.save()
        c_num = datetime.datetime.now().strftime('%Y')

        row.c_num = c_num + "-" + str(row.id)
        row.save()
        return JsonResponse({'response':True})
    except:
        return JsonResponse({'response':False})

def get_transport(request):
    user = request.user
    rows = Data.objects.filter(user_id=user.id)
    results = []
    for item in rows:
        data = {}
        data['id'] = item.id
        data['name'] = item.name       
        results.append(data)
    return JsonResponse({'results':results})

def get_contract(request):
    user = request.user
    rows = Contract.objects.filter(accepted='0')
    results = []
    for item in rows:
        data = {}
        if item.transport:
            volume = Data.objects.get(id=item.transport).volume
        else:
            volume = ""
        if str(user.id) == item.user_id:
            me = "1"
        else:
            me = "0"
        data['id'] = item.id
        data['me'] = me
        data['c_num'] = item.c_num
        data['d_address'] = item.d_address       
        data['d_city'] = item.d_city  
        data['d_date'] = item.d_date
        data['d_zipcode'] = item.d_zipcode
        data['e_address'] = item.e_address       
        data['e_city'] = item.e_city  
        data['e_date'] = item.e_date
        data['e_zipcode'] = item.e_zipcode
        data['i1_address'] = item.i1_address       
        data['i1_city'] = item.i1_city  
        data['i1_date'] = item.i1_date
        data['i1_zipcode'] = item.i1_zipcode
        data['i2_address'] = item.i2_address       
        data['i2_city'] = item.i2_city  
        data['i2_date'] = item.i2_date
        data['i2_zipcode'] = item.i2_zipcode
        data['volume'] = volume
        username = CustomUser.objects.get(id=item.user_id).first_name + " " + CustomUser.objects.get(id=item.user_id).last_name
        data['username'] = username
        results.append(data)
    return JsonResponse({'results':results})


def get_contract_user(request):
    user = request.user
    rows = Contract.objects.filter(user_id=user.id)
    results = []
    for item in rows:
        data = {}
        if item.transport:
            volume = Data.objects.get(id=item.transport).volume
        else:
            volume = ""
        
        data['id'] = item.id
        data['me'] = "1"
        data['c_num'] = item.c_num
        data['address'] = item.d_address       
        data['city'] = item.d_city  
        data['date'] = item.d_date
        data['volume'] = volume
        data['accepted'] = item.accepted
        results.append(data)
    return JsonResponse({'results':results})

def accept(request):
    user = request.user
    id = request.GET.get("id")
    row = Contract.objects.get(id=id)
    row.accepted = "1"
    row.save()
    
    whom = row.user_id       
    room = Room(who=user.id,whom=whom)
    room.save()

    return JsonResponse({'results':True})