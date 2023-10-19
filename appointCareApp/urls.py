from django.urls import path
from .views import UserView, CustomTokenObtainView,UserProfileUploadView
urlpatterns = [
path( 'user/create/', UserView.as_view(), name="create_user" ),
path('user/token/', CustomTokenObtainView.as_view(), name="get_token"),
path('user/profile/',UserProfileUploadView.as_view(),name="user_profile")
]