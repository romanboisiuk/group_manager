from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Group(models.Model):
    name = models.CharField(max_length=128)
    super_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField('User', related_name='qroups', blank=True)

    def __str__(self):
        return self.name
