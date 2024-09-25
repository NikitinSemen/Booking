from django import forms
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
        exclude = ('user',)
        widgets = {
            'date': SelectDateWidget(),
        }
