from django.contrib import admin
from bikes.models import Client, Bike, Service

admin.site.register(Client)
admin.site.register(Bike)
admin.site.register(Service)
