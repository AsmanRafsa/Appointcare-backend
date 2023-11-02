from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission


def upload_user_profiles(instance, filename):
    return "user/{filename}".format(filename=filename)


def upload_to(instance, filename):
    return "hospitals/{filename}".format(filename=filename)


SPECIALITIES = [
    ('general', 'General'),
    ('cardiologist', 'Cardiologist'),
    ('dermatologist', 'Dermatologist'),
    ('neurologist', 'Neurologist'),
    ('pediatric', 'Pediatric'),
    ('dentistry', 'Dentistry'),
    ('surgery', 'Surgery'),
    ('pharmacy', 'Pharmacy'),
    ('ct-scan', 'Ct-scan'),
    ('ultrasound', 'Ultrasound'),
    ('physiotherapy', 'Physiotherapy'),
    ('orthopaedics', 'Orthopaedics'),
    ('antenatal&postanalservices', 'Antenatal&postanalservices'),
    ('counselling', 'Counselling'),
    ('babywellclinics', 'Babywellclinics'),
    ('tBclinics', 'TBclinics'),
    ('laboratoryservices', 'Laboratoryservices'),
    ('curativeservices', 'Curativeservices'),
    ('occupationalsevices', 'Occupationalsevices'),
    ('maternity in-patient services with a word', 'Maternity in-patient services with a word'),
    
    
]



class UserProfile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=150)
    profilePic = models.ImageField(
        ("image"), upload_to=upload_user_profiles, default="user/default.png")

    def __str__(self):
        return f"{self.user.username}'s profile"


class Hospital(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, default=email)

    # password = models.CharField(max_length=128)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to '
        'each of their groups.',
        related_name='hospitals'  # Provide a custom related name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='hospitals_user_permissions'  # Provide a custom related name
    )

    def __str__(self):
        return self.name


class HospitalDetails(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    hospital_Image = models.ImageField(
        ("image"), upload_to=upload_to, default="hospitals/mayoclinic.jpg")
    hospital_Location = models.CharField(max_length=60)
    hospital_Slogan = models.CharField(max_length=100, blank=True)
    hospital_Description = models.TextField()

    def __str__(self):
        return f"{self.hospital}'s profile"


class DoctorsDetails(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name='doctors')
    doctorImage = models.ImageField(
        ("image"), upload_to=upload_to, default="hospitals/default.jpg")
    doctorName = models.CharField(max_length=50)
    doctorSpeciality = models.CharField(max_length=50, choices=SPECIALITIES)

    def __str__(self):
        return self.doctorName


class Booking(models.Model):

    hospital = models.ForeignKey(HospitalDetails, on_delete=models.CASCADE, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patientDisease = models.CharField(max_length=50)
    patientAge = models.PositiveIntegerField()
    timeBooked = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.user.username}'s - {self.hospital}"


class HospitalNotification(models.Model):
    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, null=True)
    # patient_name = models.CharField(max_length=100)
    # booked_date = models.DateTimeField()

    def __str__(self):
        return f"Hospital Notification for {self.booking}"


# class Appointment(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     date_time = models.DateTimeField()

class RatingAndReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(HospitalDetails, on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField(default=5)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
