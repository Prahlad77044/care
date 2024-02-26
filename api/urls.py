from django.urls import path, include
from .views import UserRegistrationView, UserLoginView,UserProfileViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'profile',UserProfileViewSet, basename='profile_detail')

urlpatterns = [
    path('',include(router.urls)),
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    
]
