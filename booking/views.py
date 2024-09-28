from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from booking.forms import ReservationForm
from booking.models import Reservation
from config.settings import EMAIL_HOST_USER


def home(request):
    return render(request, 'booking/base.html')


def about(request):
    return render(request, 'booking/about.html')


from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from booking.forms import ReservationForm
from booking.models import Reservation
from config.settings import EMAIL_HOST_USER


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_filter = self.request.GET.get('date_filter')
        if date_filter:
            context['reservations'] = Reservation.objects.filter(date=date_filter, reserve=True)
        else:
            context['reservations'] = Reservation.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        reservation = self.object
        confirmation_link = self.request.build_absolute_uri(
            reverse('booking:confirm_reservation', kwargs={'token': reservation.confirmation_token})
        )
        send_mail(
            subject='Подтверждение бронирования',
            message=f'Для подтверждения бронирования перейдите по ссылке: {confirmation_link}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[reservation.user.email],
            fail_silently=False,
        )

        return response

    def get_success_url(self):
        return reverse('booking:create')


class ConfirmReservationView(View):
    def get(self, request, token):
        reservation = get_object_or_404(Reservation, confirmation_token=token)
        reservation.reserve = True
        reservation.confirmation_token = None
        reservation.save()
        return redirect('booking:home')


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('users:user_profile')


class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy('users:user_profile')


class ContactView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправка сообщения на email
        send_mail(
            subject=f'Сообщение от {name}',
            message=f'От: {email}\n\n{message}',
            from_email=EMAIL_HOST_USER,
            recipient_list=['pr.pypblrka@gmail.com'],
            fail_silently=False,
        )

        return redirect('booking:home')
