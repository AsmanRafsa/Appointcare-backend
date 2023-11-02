from django.urls import path, include
from . import views
from .views import UserView, CustomTokenObtainView,UserProfileUploadView, BookingView,RatingAndReviewList,RatingAndReviewDetail
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('hospitals', HospitalViewSet)
# router.register('doctors', DoctorViewSet)
# router.register('patientprofile', BookingView)
# router.register('appointments', AppointmentViewSet)




urlpatterns = [
    path( 'user/create/', UserView.as_view(), name="create_user" ),
    path('user/token/', CustomTokenObtainView.as_view(), name="get_token"),
    path('user/profile/',UserProfileUploadView.as_view(),name="user_profile"),
    path('user/booking/', include(router.urls)),
    path('booking/', BookingView.as_view(), name='booking'),
    path('hospital/register',views.HospitalRegistrationView.as_view(),name='register'),
    path('hospital/login',views.HospitalLoginView.as_view(),name='login'),
    path('hospitaldetails/', views.HospitalView.as_view(), name='hospital'),
    path('hospitaldetails/<id>',views.SingleHospitalView.as_view(),name='singleHospital'),
    path('doctors/add/', views.DoctorDetailsView.as_view(), name='doctors'),
    path('doctorsdetail/<id>/', views.DoctorView.as_view(), name='doctordetail'),
    path('hospital-notifications/',views.HospitalNotificationView.as_view(), name='hospital-notification'),
    path('hospital-notifications/<id>/',views.HospitalNotificationDetailView.as_view(), name='hospital-notification-detail'),
    path('reviews/', RatingAndReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', RatingAndReviewDetail.as_view(), name='review-detail'),

]


if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




