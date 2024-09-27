from django.db import models
from config import settings


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.IntegerField(verbose_name='стол')
    date = models.DateField(verbose_name='дата')
    time = models.TimeField(verbose_name='время')
    guests = models.IntegerField(verbose_name='Количество гостей')
    reserve = models.BooleanField(verbose_name="зарезервирован", default=True)

    def __str__(self):
        return f'{self.user}, {self.table}'

    class Meta:
        verbose_name = 'Резерв'
        verbose_name_plural = 'Резервы'
