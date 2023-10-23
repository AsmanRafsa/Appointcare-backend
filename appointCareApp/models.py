from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return "user/{filename}".format(filename=filename)

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    phoneNumber=models.CharField(max_length=150)
    profilePic=models.ImageField(("image"),upload_to=upload_to,default="user/")
    
    def __str__(self):
        return self.user.username

