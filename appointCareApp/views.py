from django.shortcuts import render
from .model import Hospital
from rest_framework import status
from rest_framework.views import APIView 
from django.http import Http404
from rest_framework.response import Response
from .serializers import HospitalSerializer

# Create your views here.
class HospitalView(APIView):
        def get(self,request,format=None):
                hospitals=Hospital.objects.all
                serializers=HospitalSerializer(hospitals, many=True)
                return Response(serializers.data)
        


        def post(self,request,format=None):
                serializers=HospitalSerializer(data=request.data)
                if(serializers.is_valid()):
                        serializers.save()
                        return Response(serializers.data,status=status.HTTP_201_CREATED)
                return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)




class  singleHospitalView(APIView):
        def get_single_hospital(self,id): 
               try:
                   return Hospital.objects.get(id=id)
               except Hospital.DoesNotExist:
                      raise Http404



        def get(self,request,format=None):
                hospitals=Hospital.objects.all
                serializers=HospitalSerializer(hospitals, many=True)
                return Response(serializers.data)



        def put(self,request,id):
           hospital=self.get_single_hospital(id=id)
           serializer=HospitalSerializer(hospital,data=request.data)

           if (serializer.is_valid()):
             serializer.save()
             return Response(serializers.data,status=status.HTTP_200_OK)
           return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        



        


        

