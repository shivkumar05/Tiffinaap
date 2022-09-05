from tiffinapp.models.manus import  add_new_manu 
from tiffinapp.serializers import  add_new_manuSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
import datetime
from django.utils import timezone
from rest_framework import status, viewsets






class AddMannu(APIView):             
  def get(self ,request):     
    now = datetime.datetime.now()
    now = timezone.now()
    print(now)
    addmanu = add_new_manu.objects.all() 
    serializer = add_new_manuSerializer(addmanu , many=True)             
    return Response(serializer.data)
  def post(self , request):
    serializer =   add_new_manuSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()               
      return Response("add manu success fully" )  
    else:
      return Response(serializer.errors)
      
 
      
        


class Edit(APIView):
  def get(self,request,pk):  
    try:              
      ac = add_new_manu.objects.get(pk=pk)
    except add_new_manu.DoesNotExist:
      return Response(status=404)   
    serializer = add_new_manuSerializer(ac) 
    return Response(serializer.data) 
  def put(self,request ,pk): 
    try:              
      ac = add_new_manu.objects.get(pk=pk)
    except add_new_manu.DoesNotExist:
      return Response(status=404)  
    serializer = add_new_manuSerializer(ac , data = request.data )   
    if  serializer.is_valid():
        serializer.save()
        return Response("edit successfully " )          
    else:
        return Response(serializer.errors)  
          
  

    
class Filtercategery(ListAPIView):
  queryset = add_new_manu.objects.all()
  serializer_class = add_new_manuSerializer
  filter_backends = [SearchFilter]  
  search_fields = ['categery_name__name']               
  
  
  
    

              

               
    
    
