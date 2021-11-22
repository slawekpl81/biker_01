from uuid import uuid4
from django.db import models
from users.models import Business


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250, unique=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.business}'


class Bike(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    mark = models.CharField(max_length=250)
    model = models.CharField(max_length=250, blank=True)
    year = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.mark}-{self.model} of {self.owner}'


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(blank=True)
    price = models.FloatField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.client} - {self.start}'
