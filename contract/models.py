from django.db import models

class Contract(models.Model):
    id=models.AutoField(primary_key=True) 
    user_id = models.CharField(max_length=50,default='',null=True)    
    c_num = models.CharField(max_length=50,default='',null=True)    
    transport = models.CharField(max_length=50,default='',null=True)    
    d_address = models.CharField(max_length=50,default='',null=True)    
    d_city = models.CharField(max_length=50,default='',null=True)    
    d_zipcode = models.CharField(max_length=50,default='',null=True)    
    d_date = models.CharField(max_length=50,default='',null=True)    
    e_address = models.CharField(max_length=50,default='',null=True)    
    e_city = models.CharField(max_length=50,default='',null=True)    
    e_zipcode = models.CharField(max_length=50,default='',null=True)    
    e_date = models.CharField(max_length=50,default='',null=True)  
    i1_address = models.CharField(max_length=50,default='',null=True)    
    i1_city = models.CharField(max_length=50,default='',null=True)    
    i1_zipcode = models.CharField(max_length=50,default='',null=True)    
    i1_date = models.CharField(max_length=50,default='',null=True)      
    i2_address = models.CharField(max_length=50,default='',null=True)    
    i2_city = models.CharField(max_length=50,default='',null=True)    
    i2_zipcode = models.CharField(max_length=50,default='',null=True)    
    i2_date = models.CharField(max_length=50,default='',null=True)   
    accepted = models.CharField(max_length=1,default='0',null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)   
    updated_at = models.DateTimeField(blank=True,null=True)
    class Meta:
        db_table = 'contract'
