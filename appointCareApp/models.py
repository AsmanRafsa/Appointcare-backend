from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def upload_to(instance, filename):
    return "user/{filename}".format(filename=filename)

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    phoneNumber=models.CharField(max_length=150)
    profilePic=models.ImageField(("image"),upload_to=upload_to,default="user/")

    
    def __str__(self):
        return self.user.username
    

# class Hospital(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

# class Doctor(models.Model):
#     name = models.CharField(max_length=100)
#     specialty = models.CharField(max_length=100)
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

# class Appointment(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     date_time = models.DateTimeField()

class Booking(models.Model):
    # hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patientDisease=models.TextField()
    patientAge = models.PositiveIntegerField()
    timeBooked=models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.user


