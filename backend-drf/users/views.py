from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated] #only authenticated user can access this view user must be logged in 
    def get(self,request):
        serializer = UserSerializer(request.user) #request.user will give us the current logged in user permission class is giving me
                                                  #request.user  
        return Response(serializer.data)