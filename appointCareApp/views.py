
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Hospital

from appointCareApp.hospital.serializers import HospitalLoginSerializer, HospitalRegistrationSerializer

class HospitalRegistrationView(CreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalRegistrationSerializer

class HospitalLoginView(TokenObtainPairView):
    serializer_class = HospitalLoginSerializer