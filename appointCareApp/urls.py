from django.urls import path, include
from . import views
from .views import UserView, CustomTokenObtainView,UserProfileUploadView, BookingViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('hospitals', HospitalViewSet)
# router.register('doctors', DoctorViewSet)
router.register('patientprofile', BookingViewSet)
# router.register('appointments', AppointmentViewSet)


actions = {
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
}

urlpatterns = [
    path( 'user/create/', UserView.as_view(), name="create_user" ),
    path('user/token/', CustomTokenObtainView.as_view(), name="get_token"),
    path('user/profile/',UserProfileUploadView.as_view(),name="user_profile"),
    path('user/booking/', include(router.urls)),
    path('booking/', BookingViewSet.as_view(actions), name='booking'),
    path('hospital/register',views.HospitalRegistrationView.as_view(),name='register'),
    path('hospital/login',views.HospitalLoginView.as_view(),name='login'),
    path('hospitaldetails/', views.HospitalView.as_view(), name='hospital'),
    path('hospital/<id>',views.SingleHospitalView.as_view(),name='singleHospital'),
    path('doctors/add/', views.DoctorDetailsView.as_view(), name='doctors'),
    path('doctorsdetail/<id>/', views.DoctorView.as_view(), name='doctordetail'),
    path('hospital-notifications/',views.HospitalNotificationView.as_view(), name='hospital-notification'),
    path('hospital-notifications/<id>/',views.HospitalNotificationDetailView.as_view(), name='hospital-notification-detail'),

]


if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




