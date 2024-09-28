from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    table = models.IntegerField(verbose_name='стол')
    date = models.DateField(verbose_name='дата')
    time = models.TimeField(verbose_name='время')
    guests = models.IntegerField(verbose_name='Количество гостей')
    reserve = models.BooleanField(verbose_name="зарезервирован", default=False)
    confirmation_token = models.CharField(max_length=32, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user}, {self.table}'

    class Meta:
        verbose_name = 'Резерв'
        verbose_name_plural = 'Резервы'

    def save(self, *args, **kwargs):
        if not self.confirmation_token:
            self.confirmation_token = get_random_string(length=32)
        super().save(*args, **kwargs)