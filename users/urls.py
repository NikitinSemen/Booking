from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, password_recovery, UserDetailView, UserProfileView

app_name = UsersConfig.name
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='booking:home'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path("password_recovery/", password_recovery, name='password_recovery'),
    path("user_profile/", UserProfileView.as_view(template_name='users/user_profile.html'), name='user_profile'),

]
