from datetime import time

from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget, BooleanField, ModelForm

from .models import Reservation


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form_check_input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ReservationForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Reservation
        exclude = ('user', 'reserve')
        widgets = {
            'date': SelectDateWidget(),
        }

    table = forms.ChoiceField(
        choices=[(str(i), str(i)) for i in range(1, 27)],
        label='стол'
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'min': '13:00',
            'max': '23:00'
        }),
        label='Время'
    )


    def clean_time(self):
        time_value = self.cleaned_data.get('time')
        if time_value:
            if time_value < time(13, 0) or time_value > time(23, 0):
                raise ValidationError('Выберите время с 13:00 до 23:00.')
        return time_value