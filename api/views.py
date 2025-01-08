from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import CustomUser
# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_verified= True)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

