from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Booking,Hospital, HospitalDetails
        
class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    # phonenumber=serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    username=serializers.CharField(required=True)
    password=serializers.CharField(
        min_length=8,write_only=True,required=True
    )
    class Meta:
         model=User
         fields=["username","first_name","last_name","email","password"]
         
    def create(self,validated_data):
        password=validated_data.pop("password",None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super(CustomTokenObtainPairSerializer,self).validate(attrs)
        data.update({"id":self.user.id})
        data.update({"username":self.user.username})
        data.update({"email":self.user.email})
        print(data)
        
        return data
    
class RelatedUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=( "first_name","last_name","email","username","password")
 
class UserProfileSerializer(serializers.ModelSerializer):
    related_data=RelatedUserProfileSerializer(source="user", read_only=True)
    # print(related_data)
    class Meta:
        model=UserProfile
        fields='__all__'
        
        
# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = '__all__'
class RelatedHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=HospitalDetails
        fields=( "hospital", "hospital_Image", "hospital_Location",
                  "hospital_Slogan", "hospital_Description",)

class BookingSerializer(serializers.ModelSerializer):
    related_data=RelatedHospitalSerializer(source="hospital",read_only=True)
    related_userdata=RelatedUserProfileSerializer(source="user",read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
        
        

    
    
         