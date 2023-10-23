from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserProfileSerializer

# Create your views here.
class UserView(APIView):    
    permission_classes=(permissions.AllowAny,)
    authentication_classes=()
    
    def post(self,request,format='json'):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     
    
class CustomTokenObtainView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


class UserProfileUploadView(APIView):
    def put(self, request):
        dataSerializer = UserProfileSerializer(data=request.data)
        if dataSerializer.is_valid():
            dataSerializer.save()
            return Response(dataSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(dataSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

