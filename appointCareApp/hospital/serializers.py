from rest_framework import serializers
from ..models import Hospital, HospitalDetails, DoctorsDetails, HospitalNotification


class HospitalRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('email', 'phone_number', 'name', 'password')

# class RelatedHospitalLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Hospital
#         fields=('phone_number', 'name',)

class HospitalLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class RelatedHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields=('email', 'phone_number', 'name',)
        
        
        
class HospitalSerializer(serializers.ModelSerializer):

    related_data=RelatedHospitalSerializer(source="hospital", read_only=True)

    # hospital=HospitalRegistrationSerializer()
    # hospital=serializers.IntegerField()

    class Meta:
        model = HospitalDetails
        # fields = "__all__"
        fields = ("id", "hospital", "hospital_Image", "hospital_Location",
                  "hospital_Slogan", "hospital_Description","related_data")
        
# class HospitalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HospitalDetails
#         fields = ("id", "hospital", "hospital_Image", "hospital_Location",
#                   "hospital_Slogan", "hospital_Description",)


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsDetails
        fields = ('id', 'doctorImage', 'doctorName',
                  'doctorSpeciality', 'hospital',)


class HospitalNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalNotification
        fields = ('id', 'patient_name', 'booked_date', 'hospital',)
