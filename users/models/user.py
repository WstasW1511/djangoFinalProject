from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import CustomUserManager
from utils.models.abstract import AbstractUUID, AbstractTimeTracker
from django.db import models
from utils.const import Choice

class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractUUID, AbstractTimeTracker):
    phone = models.CharField(
        max_length=13,
        verbose_name='Телефон',
        unique=True
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        blank=True,
        null=True
    )

    is_staff = models.BooleanField(
        default=True,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        blank=True,
        null=True
    )
    password = models.CharField(
        max_length=100,
        default='123456'
    )

    kind = models.CharField(choices=Choice, verbose_name="status_user", max_length=50, default='User1')

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('uuid',)

    def __str__(self):
        return  self.phone
