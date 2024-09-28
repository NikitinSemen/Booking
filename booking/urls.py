from django.urls import path
from . import views
from .apps import BookingConfig
from .views import ReservationCreateView, ReservationUpdateView, ReservationDeleteView, ContactView, \
    ConfirmReservationView

app_name = BookingConfig.name
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', ReservationCreateView.as_view(), name='create'),
    path("update/<int:pk>/", ReservationUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", ReservationDeleteView.as_view(), name='delete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('confirm/<str:token>/', ConfirmReservationView.as_view(), name='confirm_reservation'),
]