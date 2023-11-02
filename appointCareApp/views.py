from django.shortcuts import render
from rest_framework.decorators import api_view
from appointCareApp.hospital.serializers import HospitalSerializer, HospitalRegistrationSerializer, HospitalLoginSerializer, DoctorsSerializer, HospitalNotificationSerializer
from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Hospital, HospitalDetails, DoctorsDetails, HospitalNotification, UserProfile, Booking,RatingAndReview
from rest_framework import generics
from .serializers import UserSerializer, UserProfileSerializer, BookingSerializer, CustomTokenObtainPairSerializer,RatingAndReviewSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password


# class HospitalRegistrationView(CreateAPIView):
#     queryset = Hospital.objects.all()
#     serializer_class = HospitalRegistrationSerializer

# class HospitalLoginView(TokenObtainPairView):
#     serializer_class = HospitalLoginSerializer

# @api_view(['GET'])
# def get_hospital_data(request):
#     print(request.user)

class HospitalRegistrationView(APIView):
    def post(self, request):
        serializer = HospitalRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Create the institution instance and hash the password
            the_hospital = serializer.save()
            the_hospital.password = make_password(request.data['password'])
            the_hospital.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalLoginView(APIView):
    # serializer_class = HospitalLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = HospitalLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hospital = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if hospital:
            login(request, hospital)

            response_data={
                'id':hospital.id,
                'email':hospital.email,
                'phone_number':hospital.phone_number,
                'name':hospital.name,
            }
            return Response(response_data,status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)



class HospitalView(APIView):
    def get(self, request, format=None):
        hospitals = HospitalDetails.objects.all()
        # print(HospitalDetails.objects.get(hospital=1))
        serializer = HospitalSerializer(hospitals, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        # hospital_id=request.data.get('hospital')
        # try:
        #     hospital_id=int(hospital_id)
        # except ValueError:
        #     return Response({'error':'Invalid hospital format'},status=status.HTTP_400_BAD_REQUEST)  
        # request.data['hospital']=hospital_id  
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleHospitalView(APIView):
    def get_single_hospital(self, id):
        try:

            return HospitalDetails.objects.get(id=id)

            return HospitalDetails.objects.get(hospital=id)

        except HospitalDetails.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        hospital = self.get_single_hospital(id)
        # print(hospital.name)
        # print(hospital.hospital.email)
        # print(hospital.hospital.phone_number)
       
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
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileUploadView(APIView):
    def get(self,request,format=None):
        users=UserProfile.objects.all()
        serializer=UserProfileSerializer(users,many=True)
        return Response(serializer.data)

    def put(self, request):
        dataSerializer = UserProfileSerializer(data=request.data)
        if dataSerializer.is_valid():
            dataSerializer.save()
            return Response(dataSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(dataSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BookingView(APIView):
    def get(self,request,format=None):
        bookings=Booking.objects.all()
        serializer=BookingSerializer(bookings,many=True)
        return Response(serializer.data)
    # def put(self, request):
    #     dataSerializer = BookingSerializer(data=request.data)
    #     if dataSerializer.is_valid():
    #         dataSerializer.save()
    #         return Response(dataSerializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(dataSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format='json'):
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      
    


class RatingAndReviewList(generics.ListCreateAPIView):
    # queryset = RatingAndReview.objects.all()
    def post(self,request,format='json'):
        serializer_class = RatingAndReviewSerializer
        serializer=serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)      
    
    

class RatingAndReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RatingAndReview.objects.all()
    serializer_class = RatingAndReviewSerializer
