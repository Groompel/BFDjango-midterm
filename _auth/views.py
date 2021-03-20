from _auth.models import UserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

# Create your views here.

# Register functionality
class CreateUserView(viewsets.generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
