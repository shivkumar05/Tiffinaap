import email
from django.db import models

class center(models.Model):
    city = models.CharField(unique=True, max_length=100)  
    def __str__(self):
        return str(self.city)
    
    

class account(models.Model):
    username = models.CharField(max_length=100 , null=True)
    phone_number = models.IntegerField(null=True)
    choose_center = models.ForeignKey(center  , on_delete=models.CASCADE)
    email = models.EmailField(blank=True , null=True)
    password = models.CharField(max_length=100 , null=True)
    
    def __str__(self):
        return str(self.username)
    
    
class sigin(models.Model):
    email = models.EmailField(blank=True , null=True)  
    password = models.CharField(max_length=100, null=True) 
    choose_center = models.ForeignKey(center, on_delete=models.CASCADE ,default=1)

    
    def __str__(self):
       return str(self.email)
   
    def create(self , validated_data):
        user = sigin.objects.create(email = validated_data['email'])   
        user.set_password(validated_data['password'])
        user.save()
        return user           
    
