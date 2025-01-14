from django.shortcuts import render
from rest_framework import generics, viewsets, status
from .serializers import UserSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from api.models import CustomUser
from rest_framework.response import Response

# Create your views here.

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_verified= True)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterVIew(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny)
    serializer_class = RegisterSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == "GET":
        response = f"Hey {request.user}, You are seeeing the GET request"
        return Response({'response':response}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        test = request.POST.get
        response = f"Hey {request.user}, You are seeeing the GET request"
        return Response({'response':response}, status=status.HTTP_200_OK)



