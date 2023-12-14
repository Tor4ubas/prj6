
from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email-адрес')

    # phone = models.CharField(max_length=35, verbose_name='Номер телефона', null=True)
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    avatar = models.ImageField(upload_to='user_app/', verbose_name='Аватар')
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    email_verification = models.BooleanField(default=False, verbose_name='Верификация почты')
    code_verification = models.CharField(max_length=20, verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
