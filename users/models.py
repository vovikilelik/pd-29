from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.TextField()
    lat = models.CharField(max_length=20)
    lon = models.TextField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class User(AbstractUser):

    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICES = [(MEMBER, 'Участник'), (MODERATOR, 'Модератор'), (ADMIN, 'Админ')]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=MEMBER)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)

    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
