from django.db import models


def upload_to(instance,filename):
    return "hospitals/{filename}".format(filename=filename)
# Create your models here.
class Hospital(models.Model):
    hospital_Name=models.CharField(max_length=60)
    hospital_Image=models.ImageField(("image"),upload_to=upload_to,default="hospitals/mayoclinic.jpg")
    hospital_Location=models.CharField(max_length=60)
    hospital_Slogan=models.CharField(max_length=100)
    hospital_Detail=models.TextField()
    