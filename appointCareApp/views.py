from django.shortcuts import render
from appointCareApp.hospital.serializers import HospitalSerializer,HospitalRegistrationSerializer,HospitalLoginSerializer,DoctorsSerializer,HospitalNotificationSerializer
from rest_framework import permissions, status,viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Hospital,HospitalDetails,DoctorsDetails,HospitalNotification, UserProfile, Booking
from rest_framework import generics
from .serializers import UserSerializer,UserProfileSerializer, BookingSerializer, CustomTokenObtainPairSerializer



class HospitalRegistrationView(CreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalRegistrationSerializer

class HospitalLoginView(TokenObtainPairView):
    serializer_class = HospitalLoginSerializer



class HospitalView(APIView):
    def get(self, request, format=None):
        hospitals = HospitalDetails.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleHospitalView(APIView):
    def get_single_hospital(self, id):
        try:
            return Hospital.objects.get(id=id)
        except Hospital.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        hospital = self.get_single_hospital(id)
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        hospital = self.get_single_hospital(id)
        serializer = HospitalSerializer(hospital, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DoctorDetailsView(APIView):
    def get(self, request, format=None):
        doctors = DoctorsDetails.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorView(APIView):
    
    def get_object(self, id):
        try:
            return DoctorsDetails.objects.get(id=id)
        except DoctorsDetails.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        doctor = self.get_object(id)
        serializer = DoctorsSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        doctor = self.get_object(id)
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        doctor = self.get_object(id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class HospitalNotificationView(generics.ListCreateAPIView):
    queryset = HospitalNotification.objects.all()
    serializer_class = HospitalNotificationSerializer

class HospitalNotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospitalNotification.objects.all()
    serializer_class = HospitalNotificationSerializer


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


# class HospitalViewSet(viewsets.ModelViewSet):
#     queryset = Hospital.objects.all()
#     serializer_class = HospitalSerializer

# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
