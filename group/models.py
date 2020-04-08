from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Person(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Group(models.Model):
    name = models.CharField(max_length=128)
    super_admin = models.CharField(max_length=128)
    users = models.ManyToManyField('Person', related_name='qroups', blank=True)

    def __str__(self):
        return self.name
