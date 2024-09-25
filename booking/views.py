from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, UpdateView, ListView

from booking.forms import ReservationForm
from booking.models import Reservation


def home(request):
    return render(request, 'booking/base.html')


def about(request):
    return render(request, 'booking/about.html')


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm

    def get_success_url(self):
        return reverse('booking:reservation_for', kwargs={'pk': self.object.pk})


class ReservationUpdateView(UpdateView):
    model = Reservation


class ReservationListView(ListView):
    model = Reservation

