from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User  
from tiffinapp.serializers import ChangeEmailSerializer


class  ChangeEmailView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeEmailSerializer