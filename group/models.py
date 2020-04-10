from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Group(models.Model):
    name = models.CharField(max_length=128)
    super_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    admins = models.ManyToManyField(User, blank=True, related_name='group_admins')
    members = models.ManyToManyField(User, blank=True, related_name='group_members')

    def __str__(self):
        return self.name
