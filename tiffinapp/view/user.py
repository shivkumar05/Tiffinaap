import email
from email import message
from wsgiref import validate
from tiffinapp.models.users import  sigin , account 
from tiffinapp.serializers import  UserSerializer, accountSerializer , siginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework import generics , permissions
from django.views import generic
from rest_framework import routers, serializers, viewsets







class RegisterUser(APIView):
  def post(self , request):
    serializer = UserSerializer(data = request.data) 
    if not serializer.is_valid():
      return Response({'status':403 , 'errors': serializer.errors , 'massage':'data is not valid '})          
    else:
      serializer.save()
      user = User.objects.get(username = serializer.data['username'])
      refresh = RefreshToken.for_user(user)
      return Response({'status':403 , 'playload': serializer.data , 'refresh': str(refresh),'access': str(refresh.access_token) ,'message':'your data is submited'})


class Account1(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
       
  def get(self , request ):
    accounts = account.objects.all() 
    serializer = accountSerializer(accounts , many = True) 
    return Response(serializer.data) 
  def post(self , request ) :
    serializer = accountSerializer(data=request.data) 
    if serializer.is_valid():
      email = serializer.validated_data.get('email')   
      if account.objects.filter(email = email).exists():
        raise serializers.ValidationError({'email' , ('Email is already in uses')}) 
      serializer.save()
      return Response("account create successfully") 
                  
    else:
      return Response(serializer.errors)     
    
    
    
class EditProfile(APIView):
  def get(self,request,pk):  
    try:              
      ac = account.objects.get(pk=pk)
    except account.DoesNotExist:
      return Response(status=404)   
    serializer = accountSerializer(ac) 
    return Response(serializer.data) 
  def put(self,request ,pk): 
    try:              
      ac = account.objects.get(pk=pk)
    except account.DoesNotExist:
      return Response(status=404)  
    serializer = accountSerializer(ac , data = request.data )   
    if  serializer.is_valid():
        serializer.save()
        return Response("edit successfully " )          
    else:
        return Response(serializer.errors)  
          
  
            
                    
                             

class sig(APIView):
  def get(self , request):
    signs = sigin.objects.all()
    serializer = siginSerializer(signs , many = True) 
    return Response(serializer.data)
  
  def post(self , request):
    serializer = siginSerializer(data = request.data) 
    if not serializer.is_valid():
      return Response({'status':403 , 'errors': serializer.errors , 'massage':'data is not valid '})          
    else:
      serializer.save()
      user = sigin.objects.filter(email = serializer.data['email']).first()
      refresh = RefreshToken.for_user(user)
      return Response("sigin successfully")
      #return Response({'status':403 , 'playload': serializer.data , 'refresh': str(refresh),'access': str(refresh.access_token) ,'message':'your data is submited'})


            
                                                            
                                        
        
class  UserListView(APIView):       
  def get(self ,request):
    users = User.objects.all()   
    serializer = UserSerializer(users , many=True)
    return Response(serializer.data , safe=False)       
  
class ChangePassword(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = siginSerializer
    model = sigin
    #permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

     
          
  



         
                            
 




  