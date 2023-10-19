from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hospitals/',views.HospitalView.as_View(),name='hospitals'),
    path('hospitals/<id>',views.SingleHospitalView.as_View(),name='singleHospital'),

]


if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)