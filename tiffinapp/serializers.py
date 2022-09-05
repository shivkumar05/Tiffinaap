from asyncore import read
from pydantic import validate_email
from requests import request
from .models.manus import *
from .models.users import *
from .models.orderlist import *
from .models.category import *
from rest_framework import serializers
from rest_framework import serializers 
from django.contrib.auth.models import User  
from .models.orderlist import OderItem , Cart 


class centerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = center
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']   
        
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])  
        user.set_password(validated_data['password']) 
        user.save()
        return user         
    
               
            
class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = "__all__"  
                      
   
    # def validate(self, attrs):
    #     if account.objects.filter(email = attrs['email']).exists():
    #         raise serializers.ValidationError({'email' , ('Email is already in uses')})              
    #     return super().validate(attrs)
    
    def create(self, validated_data):
        return account.objects.create(**validated_data)
    
    def update(self , ac , validated_data):
        newadd_manu = account(**validated_data)
        newadd_manu.id = ac.id;
        newadd_manu.save()
        return  newadd_manu 
    
      
    
    
class siginSerializer(serializers.ModelSerializer):
    class Meta:
        model = sigin
        fields = "__all__"
        
    def get_sensor(self, obj):
        return str(obj.choose_center)    
        
         
    def validate(self, attrs): 
        if account.objects.filter(email = attrs['email']).exists():
           return super().validate(attrs)                   
        else:        
          raise serializers.ValidationError({'email' , ('Email is not valid for sigin')})              
        
    
    
    def create(self, validated_data):
       return sigin.objects.create(**validated_data)
    
                 
                     

class add_new_manuSerializer(serializers.ModelSerializer):  
    categery_name = serializers.CharField(max_length=100)               
    class Meta:
        model = add_new_manu 
        fields = ['image' ,'Tiffin_Name' ,'categery_name' ,'Tiffin_Price' ,'Offer_price' ,'start_time','end_time','Description'] 
                 
    def create(self, validated_data):
        return add_new_manu.objects.create(**validated_data)
    
    def update(self , ac , validated_data):
        newadd_manu = add_new_manu(**validated_data)
        newadd_manu.id = ac.id;
        newadd_manu.save()
        return  newadd_manu
    
   
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"             
             
                    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart 
        fields = '__all__' 
                 
                 
class OrderItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer() 
    product =  add_new_manuSerializer()       
    class Meta:
        model = OderItem
        fields = '__all__'             
                    
   
    
              
          
     
class ChangePasswordSerializer(serializers.Serializer):
    model = sigin
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
                     
                     
# class ChangeEmailSerializer(serializers.Serializer):
#     model = account
#     """
#     Serializer for password change endpoint.
#     """
#     old_email = serializers.CharField(required=True)
#     new_email = serializers.CharField(required=True)
                     
                        
                     
class ChangeEmailSerializer(serializers.ModelSerializer):
    old_email = serializers.CharField(write_only=True, required=True, validators=[validate_email])
    email = serializers.CharField(write_only=True, required=True)
    new_email = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('old_email', 'email', 'new_email')

    def validate(self, attrs):
        if attrs['old_email'] != attrs['email']:
            raise serializers.ValidationError({"email": "email fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_email": "Old email is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['email'])
        instance.save()
        return instance
              