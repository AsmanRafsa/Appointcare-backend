from rest_framework import serializers
from .models import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Hospital
        fields=("id","hospital_Name","hospital_Image","hospital_Location","hospital_Slogan","hospital_Detail",)
