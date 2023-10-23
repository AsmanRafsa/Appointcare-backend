from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserView, CustomTokenObtainView,UserProfileUploadView, BookingViewSet
from . import views

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
path('booking/', BookingViewSet.as_view(actions), name='booking')

]
