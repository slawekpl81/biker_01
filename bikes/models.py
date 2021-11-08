from uuid import uuid4
from django.db import models


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Bike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    mark = models.CharField(max_length=250)
    model = models.CharField(max_length=250, blank=True)
    year = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.mark}-{self.model} of {self.owner}'


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(blank=True, default=None)
    price = models.FloatField(blank=True, default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.client} - {self.start}'
