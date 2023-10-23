from django.contrib import admin
from .models import Hospital, HospitalDetails,DoctorsDetails,HospitalNotification, UserProfile,Booking

# Register your models here.
admin.site.register(HospitalDetails)
admin.site.register(Hospital)
admin.site.register(DoctorsDetails)
admin.site.register(HospitalNotification)
admin.site.register(UserProfile)
admin.site.register(Booking)
