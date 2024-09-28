from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=12, verbose_name='Имя')
    last_name = models.CharField(max_length=15, verbose_name='Фамилия')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE, help_text='введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='Аватар')
    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
