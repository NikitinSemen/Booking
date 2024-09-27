from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, UpdateView, ListView

from booking.forms import ReservationForm
from booking.models import Reservation


def home(request):
    return render(request, 'booking/base.html')


def about(request):
    return render(request, 'booking/about.html')


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('booking:create')
