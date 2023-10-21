from django.contrib import admin
from .models import Hospital, HospitalDetails,DoctorsDetails,PatientDetails
# Register your models here.
admin.site.register(HospitalDetails)
admin.site.register(Hospital)
admin.site.register(DoctorsDetails)
admin.site.register(PatientDetails)






