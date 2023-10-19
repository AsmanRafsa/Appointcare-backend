from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('hospitals/',views.HospitalView.as_view(),name='hospitals'),
    # path('hospitals/<id>',views.SingleHospitalView.as_view(),name='singleHospital'),
    # path('new-hospital/', views.NewHospitalView.as_view(), name="new-hospital"),
    # path('hospitaladmin-login/',views.HospitalLoginView.as_view(),name="hospitallogin")
     path('hospital/register',views.HospitalRegistrationView.as_view(),name='register'),
    path('hospital/login',views.HospitalLoginView.as_view(),name='login'),
   

]


if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)