from django.urls import path
from account.views import UserRegistrationView, UserLoginView, UserProfile
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfile.as_view(), name='profile'),
]
