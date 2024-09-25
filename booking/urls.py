from django.urls import path
from . import views
from .apps import BookingConfig
from .views import ReservationCreateView

app_name = BookingConfig.name
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', ReservationCreateView.as_view(), name='create')
]