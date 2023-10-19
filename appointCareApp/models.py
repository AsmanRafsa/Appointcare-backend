from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin



def upload_to(instance,filename):
    return "hospitals/{filename}".format(filename=filename)

# Create your models here.
class NewHospital(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email address"), unique=True)
    hospitalName = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    USERNAME_FIELD = "email"
   
    def __str__(self):
        return self.email

class Hospital(models.Model):
    hospital_Image=models.ImageField(("image"),upload_to=upload_to,default="hospitals/")
    hospital_Location=models.CharField(max_length=60)
    hospital_Slogan=models.CharField(max_length=100)
    hospital_Detail=models.TextField()
    