from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=128)
    super_admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    admins = models.ManyToManyField(User, related_name='qroup_admins')
    users = models.ManyToManyField(User, related_name='qroup_users')

    def __str__(self):
        return self.name
