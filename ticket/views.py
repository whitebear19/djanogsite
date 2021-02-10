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


def dashboard(request):
    
    user = request.user 
    if not request.user.is_authenticated:
        return redirect('/login')
       
    
    return render(request,'ticket/dashboard.html',{}) 
