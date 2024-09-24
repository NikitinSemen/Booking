from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    confirmed = models.BooleanField(default=False)



