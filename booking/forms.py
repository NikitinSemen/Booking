from datetime import datetime, time
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
        exclude = ('user', 'reserve', 'confirmation_token')
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

    def clean(self):
        cleaned_data = super().clean()
        user = self.instance.user if self.instance.pk else self.initial.get('user')
        table = cleaned_data.get('table')
        date = cleaned_data.get('date')
        time_reserve = cleaned_data.get('time')

        if date and time:
            current_datetime = datetime.now()
            if date < current_datetime.date() or (date == current_datetime.date() and time_reserve < current_datetime.time()):
                raise ValidationError('Нельзя забронировать на прошедшее время.')

        existing_reservations = Reservation.objects.filter(table=table, date=date)
        if self.instance.pk:
            existing_reservations = existing_reservations.exclude(pk=self.instance.pk)
        if existing_reservations.exists():
            raise ValidationError('Этот стол уже забронирован на выбранную дату.')

        user_reservations = Reservation.objects.filter(user=user, date=date)
        if self.instance.pk:
            user_reservations = user_reservations.exclude(pk=self.instance.pk)
        if user_reservations.exists():
            raise ValidationError('Вы уже забронировали стол на эту дату.')

        return cleaned_data