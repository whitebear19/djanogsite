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

from .forms import LoginForm, RegisterForm

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

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def check_auth(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        return True

PAGINATION_COUNT = 21
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/{ip}?access_key=48ff15e0e6d7fde5fbcf780a6adbc287"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_different_time(orgtime):
    
    curtime = datetime.datetime.now()
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    date1 = orgtime.strftime('%Y-%m-%d %H:%M:%S.%f')
    date2 = curtime.strftime('%Y-%m-%d %H:%M:%S.%f')
    diff = datetime.datetime.strptime(date2, datetimeFormat)\
        - datetime.datetime.strptime(date1, datetimeFormat)    
    
    result = ''
    if(int(diff.days) > 0):
        result = diff.days       
        if(int(result)>30):
            result = math.ceil(int(result)/30)
            result = str(result)+"Months"
        else:
            result = str(result)+"Days"
    else:
        result = diff.seconds
        if(int(result) > 3600):
            result = math.ceil(int(result)/3600)
            result = str(result)+"Hours"
        else:
            result = math.ceil(int(result)/60)+1
            result = str(result)+"Mins"
    return result

def get_date_str(orgtime):
    result = ''
    curtime = datetime.datetime.now()
    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    date1 = orgtime.strftime('%Y-%m-%d %H:%M:%S.%f')
    date2 = curtime.strftime('%Y-%m-%d %H:%M:%S.%f')
    diff = datetime.datetime.strptime(date2, datetimeFormat)\
        - datetime.datetime.strptime(date1, datetimeFormat)        
    if(int(diff.days) < 1):
        curDate = curtime.strftime('%d')
        orgDate = orgtime.strftime('%d')
        if curDate == orgDate:
            result = 'Today'
        else:
            result = 'Yesterday'
    elif (int(diff.days) < 2):
        curDate = curtime.strftime('%d')
        orgDate = orgtime.strftime('%d')
        if int(curDate) > int(orgDate):
            if (int(curDate)-int(orgDate)) > 1:
                result = orgtime.strftime('%d%m%Y')
            else:
                result = 'Yesterday'
        else:
            result = 'Yesterday'
    else:
        result = orgtime.strftime('%d/%m/%Y')
    return result

def get_time_str(orgtime):
    result = orgtime.strftime('%H:%M')
    return result

def send_code_email(email,code):
    try:
        subject = 'Email Verify Code' 
        html_message = render_to_string('email/verify.html', {'code': code})
        plain_message = strip_tags(html_message)
        from_email = 'welcome.com'
        send_mail(subject, plain_message, from_email, [email], html_message=html_message) 
        return True
    except:
        return False

def verify_resend(request):
    results = False
    try:        
        user = request.user
        verified_code = str(random.randint(100000,999999))

        
        user.verified_code = verified_code            
        user.save()            
        send_code_email(user.email,verified_code) 
        results = True
        
        return JsonResponse({'results':results,'which':'e','auth':True})
    except:
        return JsonResponse({'results':results,'which':"",'auth':False})



def verify_confirm(request):
    results = False
    try:
        code = request.POST.get('code')
        user = request.user
        if(user.verified_code == code):
            user.verified = '1'
            user.save()
            results = True
        else:
            results = False
        return JsonResponse({'results':results,'auth':True})
    except:
        return JsonResponse({'results':results,'auth':False})



def login_custom(request):
    if not request.user.is_authenticated:
        return render(request,'registration/login.html')
    else:
        user = request.user     
        if user.verified == "0":
            return redirect('/confirm')
        else:
            return redirect('/home')  
        
    

def register_custom(request):
    if not request.user.is_authenticated:
        return render(request,'registration/register.html') 
    else:
        user = request.user        
        if user.verified == "0":
            return redirect('/confirm')
        else:
            return redirect('/home')  
            
def confirm(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:        
        return render(request,'registration/confirm.html') 

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:        
        return redirect('/home')

def home(request):
           
    return render(request,'home/dashboard.html',{}) 

def terms(request):
           
    return render(request,'home/terms.html',{}) 

def profile(request):
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('/login')
       
    page = request.GET.get('page')
    return render(request,'account/profile.html',{'page':page}) 

# -------------------------------------------------------
def logout(request):
    if request.method == 'POST':
        auth_views.auth_logout(request)
    return redirect('/home')

def messages(request): 
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user
    if user.verified == "0":
        return redirect('/confirm')
    else:
        return render(request,'data/messages.html',{}) 


# ajax_part

def upload_avatar(request):
    try:
        user = request.user
        is_store = request.POST.get('is_store') 
        
        if is_store == '1':                
            user.avatar = request.FILES.get('attach')
            user.save()
        else:                
            user.avatar = ''
            user.save()
        return JsonResponse({'response':True})
    except:
        return JsonResponse({'response':False})

def store_basicinfo(request):    
    email = request.POST.get('email')
       
    emailcount = CustomUser.objects.filter(email=email).count()
    user = request.user
    result={}
    
    if user.email == email:        
        emailcount = 0
   
    result['emailcount'] = emailcount
    if emailcount > 0 :
        return JsonResponse({'response':result})
    else:  
        
        user.email = email
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        
        user.gender = request.POST.get('gender')
        user.location = request.POST.get('location')       
       
        user.save()
        
        return JsonResponse({'response':result})

def get_phoneCode(request):
    code = ''
    # ipaddress = get_client_ip(request) 
    ipaddress = '188.43.235.177'
    geo_info = get_geolocation_for_ip(ipaddress)
    results=json.dumps(geo_info) 
    results=json.loads(results)
    if results['country_code']:
        code = results['country_code']
    else:
        code = 'fr'
    return JsonResponse({'results':code})

def check_login(request):
    email = request.POST.get('email').replace(" ", "")
    password = request.POST.get('password')
    which = request.POST.get('which')
    results = {}
    
    is_phone = 0
    is_email = 0
    if which == 'phone':
        is_phone = CustomUser.objects.filter(phone=email).count()
        if is_phone > 0:
            cur_user = CustomUser.objects.get(phone=email)
    else:
        is_email = CustomUser.objects.filter(email=email).count()
        if is_email > 0:
            cur_user = CustomUser.objects.get(email=email)
    
    results['is_phone'] = is_phone
    results['is_email'] = is_email
    results['is_pass'] = '1'
    results['is_active'] = '1'
    
    
    if is_phone == 0 and is_email == 0:        
        return JsonResponse({'results':results})
    else: 
        
        if cur_user.is_active:            
            user = authenticate(username=cur_user.username,password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'results':results})

            else:            
                results['is_pass'] = '0'
                return JsonResponse({'results':results})    
        else:            
            results['is_active'] = '0'
            return JsonResponse({'results':results}) 

def check_register(request):    
    # try:
    firstname = request.POST.get('firstname').replace(" ", "")
    lastname = request.POST.get('lastname').replace(" ", "")
    email = request.POST.get('email').replace(" ", "")
    phone = request.POST.get('phone').replace(" ", "")
    phonecode = request.POST.get('phonecode')
    
    password = request.POST.get('password1')

    professional = request.POST.get('professional')
    address = request.POST.get('address')
    city = request.POST.get('city')
    zipcode = request.POST.get('zipcode')
    company = request.POST.get('company')
    tel_fix = request.POST.get('tel_fix')
    siret = request.POST.get('siret')
    which = request.POST.get('which')
    if which == 'phone':
        is_phone = CustomUser.objects.filter(phone=phone).count()
        is_email = 0
    else:
        is_phone = 0
        is_email = CustomUser.objects.filter(email=email).count()

    results = {}
    results['is_phone'] = is_phone
    results['is_email'] = is_email
    results['which'] = which
    
        
    verified_code = str(random.randint(100000,999999))
    if is_phone > 0 or is_email > 0:
        return JsonResponse({'results':results})
    else:      
        
        row = CustomUser(password=make_password(password),username=datetime.datetime.now().strftime("%m%d%Y%H%M%S"),is_superuser=0,is_staff=0,is_active=1,first_name=firstname,last_name=lastname,email=email,phone=phone,phone_code=phonecode,professional=professional,address=address,city=city,zipcode=zipcode,company=company,tel_fix=tel_fix,siret=siret)
        row.save()  
        user = authenticate(username=row.username,password=password)
        login(request, user)
        send_code_email(email,verified_code) 

        return JsonResponse({'results':results})
    # except:
    #     return JsonResponse({'results':False})


def close_account(request):
    user = request.user
    try:
        user.is_active = "0"
        user.save()
        auth_views.auth_logout(request)
        return JsonResponse({'results':True})
    except:
        return JsonResponse({'results':False})