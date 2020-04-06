from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    super_admin = models.ForeignKey(Person, on_delete=models.CASCADE)
    users = models.ManyToManyField(Person, related_name='qroup_users', blank=True)

    def __str__(self):
        return self.name
