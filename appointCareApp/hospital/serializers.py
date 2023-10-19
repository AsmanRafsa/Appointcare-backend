from rest_framework import serializers
from .models import Hospital,NewHospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Hospital
        fields=("id","hospital_Image","hospital_Location","hospital_Slogan","hospital_Detail",)



class NewHospitalSerializer(serializers.ModelSerializer):
     class Meta:
         Model=NewHospital 
         fields=('id','email','hospitalName','phonenumber','password') 
    
class UserAuthenticationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15)
