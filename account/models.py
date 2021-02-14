from django.db import models
import sys
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), null=True,default='')
    avatar = models.ImageField(upload_to='avatar',default='', null=True)
    back = models.ImageField(upload_to='back',default='', null=True)
    gender = models.CharField(max_length=20,default='', null=True)
    professional = models.CharField(max_length=20,default='', null=True)
    professional = models.CharField(max_length=20,default='', null=True)
    address = models.CharField(max_length=250,default='', null=True)      
    city = models.CharField(max_length=50,default='', null=True)      
    zipcode = models.CharField(max_length=10,default='', null=True)      
    company = models.CharField(max_length=50,default='', null=True)      
    phone = models.CharField(max_length=20,default='', null=True)
    phone_code = models.CharField(max_length=5,default='', null=True)
    tel_fix = models.CharField(max_length=50,default='', null=True)
    siret = models.CharField(max_length=50,default='', null=True)
     
    created_at = models.DateTimeField(auto_now_add=True,blank=True)


 
     
