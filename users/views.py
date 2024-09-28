import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
import secrets

from booking.models import Reservation
from users.forms import UserRegisterForm, UserPassForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Здравствуйте, пройдите по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['reservations'] = Reservation.objects.filter(user=self.request.user)
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_profile')


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def password_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        print(f'Получен адрес {email}')

        user = get_object_or_404(User, email=email)

        print(f'Пользователь {user}')

        password = ''

        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(12))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 3):
                break

        print(f'Пароль {password}')

        message = f"Привет, держи новый сложный 12-ти символьный пароль, который ты тоже забудешь: {password}. \
                    Если вы не запрашивали восстановление пароля, просто игнорируйте это сообщение."

        print(f'Пароль {message}')

        send_mail(
            subject='Восстановление пароля',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )

        user.set_password(password)
        user.save()
        return redirect(reverse('users:login'))

    return render(request, 'users/password_recovery.html')
