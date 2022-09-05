from unicodedata import category
from django.db import models
from tiffinapp.models.category import Category
from .users import center


class add_new_manu(models.Model):           
    image = models.ImageField(upload_to ="product" ,null =True , blank = True)  
    Tiffin_Name = models.CharField(max_length=100 , null=True) 
    categery_name = models.ForeignKey(Category, on_delete=models.CASCADE ,default=1)
    Tiffin_Price = models.FloatField(null = True) 
    Offer_price = models.FloatField(null=True) 
    choose_center = models.ForeignKey(center, on_delete=models.CASCADE ,default=1)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    Description = models.CharField(max_length=100, null=True)
    
    
    def __str__(self):
        return str(self.Tiffin_Name )
    
   