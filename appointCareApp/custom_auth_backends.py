from django.contrib.auth.backends import ModelBackend
from .models import Hospital
from django.contrib.auth.hashers import check_password


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            hospital = Hospital.objects.get(email=email)
        except Hospital.DoesNotExist:
            return None

        # if hospital.check_password(password):
        if check_password(password, hospital.password):
            return hospital

    def get_user(self, user_id):
        try:
            return Hospital.objects.get(pk=user_id)
        except Hospital.DoesNotExist:
            return None