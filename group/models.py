from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Group(models.Model):
    name = models.CharField(max_length=128)
    super_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User,
        blank=True,
        through='Membership',
        related_name='group_members',
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    ADMIN = 'admin'
    GENERAL = 'general'
    REQUESTED = 'requested'
    PERMISSION_CHOICES = [
        (ADMIN, 'Admin'),
        (GENERAL, 'General'),
        (REQUESTED, 'Requested'),
    ]
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member_permission = models.CharField(
        max_length=10,
        choices=PERMISSION_CHOICES,
        default=REQUESTED,
    )
