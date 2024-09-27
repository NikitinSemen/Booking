from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from booking.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'password1', 'password2')



class UserPassForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', )