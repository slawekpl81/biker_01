from django.shortcuts import render
from django.views.generic import ListView, DetailView

from bikes.models import Client, Bike, Service


def start(request):
    return render(request, 'start.html')


class ClientsListView(ListView):
    model = Client
    template_name = 'list_view.html'
    context_object_name = 'clients_list'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class BikesListView(ListView):
    model = Bike
    template_name = 'list_view.html'
    context_object_name = 'bikes_list'


class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'


class ServicesListView(ListView):
    model = Service
    template_name = 'list_view.html'
    context_object_name = 'services_list'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
