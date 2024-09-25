from django import forms
from django.forms import SelectDateWidget

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ('user', )
        widgets = {
            'date': SelectDateWidget(),
        }
