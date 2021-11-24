from django.forms import ModelForm
from bikes.models import Client, Bike, Service


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'description']


class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = ['mark', 'model', 'year', 'description']


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['end', 'price', 'description']
