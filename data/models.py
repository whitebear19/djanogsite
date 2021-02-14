from django.db import models

class Data(models.Model):
    id=models.AutoField(primary_key=True) 
    user_id = models.CharField(max_length=50,default='',null=True)    
    name = models.CharField(max_length=50,default='',null=True)    
    volume = models.CharField(max_length=20,default='',null=True)    
    available = models.CharField(max_length=20,default='',null=True)    
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)   
    updated_at = models.DateTimeField(blank=True,null=True)
    class Meta:
        db_table = 'data'