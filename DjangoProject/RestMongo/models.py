from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False,default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    
    def save(self,*args,**kwargs):
        print("Inside Save ")
        super(Tutorial,self).save(using="mongo_db")
        