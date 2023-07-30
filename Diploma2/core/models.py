from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_('логин'), unique=True, max_length=70)
    first_name = models.CharField(_('Имя'), max_length=35)
    last_name = models.CharField(_('Фамилия'), max_length=35)
    email = models.EmailField(_('Email'), max_length=40)

    def __str__(self):
        return self.username


    objects = UserManager()

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'