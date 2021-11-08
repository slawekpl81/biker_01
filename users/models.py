from django.contrib.auth.models import User
from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class BusinessEmployee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
