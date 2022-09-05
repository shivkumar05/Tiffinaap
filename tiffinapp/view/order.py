from django.shortcuts import  redirect, render
from numpy import product
from tiffinapp.models.manus import add_new_manu
from tiffinapp.serializers import add_new_manuSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


def post(self , request):
  product = request.POST.get("add_new_manu")     
  myorder = request.session.get('myorder')
  if myorder:
    quantity = myorder.get(product) 
    if quantity:
      myorder[product] =  quantity+1            
    else:
       myorder[product] = 1
  else:
    myorder = {}   
    myorder[product]= 1 
  request.session['myorder'] = myorder
  return redirect('homepage')          
                        
  
    
    
   