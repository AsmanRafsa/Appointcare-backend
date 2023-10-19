from rest_framework import serializers
from ..models import Hospital

class HospitalRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('email', 'phone_number', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        hospital = Hospital(**validated_data)
        hospital.set_password(password)
        hospital.save()
        return hospital

class HospitalLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)