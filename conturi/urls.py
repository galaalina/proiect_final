from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, ProfileUpdateView

app_name = 'conturi'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
]
