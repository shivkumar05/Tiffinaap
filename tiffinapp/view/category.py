from requests import Response
from tiffinapp.serializers import  add_new_manuSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class Category(APIView):  
  def get(request , pk):   
    try:              
      ac = add_new_manuSerializer.objects.get(category_id=pk)
    except add_new_manuSerializer.DoesNotExist:
      return Response(status=404)
    serializer = add_new_manuSerializer(ac)
    return  Response(serializer.data)
  
    
      
     

