from django.shortcuts import render
from django.views.generic import ListView, DetailView

from bikes.models import Client, Bike, Service


def start(request):
    return render(request, 'start.html')


class ClientsListView(ListView):
    model = Client
    template_name = 'list_view.html'
    context_object_name = 'clients_list'

    def get_context_data(self, **kwargs):
        login_user = self.request.user
        business = login_user.employee_of.business
        business_clients = Client.objects.filter(business=business)
        return {'clients_list': business_clients}


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


def client_extra_view(request, pk):
    client = Client.objects.get(pk=pk)
    bikes = Bike.objects.filter(owner=client)
    services = Service.objects.filter(client=client)
    return render(request, 'client_detail.html', {'client': client, 'bikes': bikes, 'services': services})


class BikesListView(ListView):
    model = Bike
    template_name = 'list_view.html'
    context_object_name = 'bikes_list'

    def get_context_data(self):
        login_user = self.request.user
        business = login_user.employee_of.business
        business_clients = Client.objects.filter(business=business)
        business_bikes = Bike.objects.filter(owner__business__client__in=business_clients).distinct()
        return {'bikes_list': business_bikes}


class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'


class ServicesListView(ListView):
    model = Service
    template_name = 'list_view.html'
    context_object_name = 'services_list'

    def get_context_data(self, **kwargs):
        login_user = self.request.user
        business = login_user.employee_of.business
        business_clients = Client.objects.filter(business=business)
        services_list = Service.objects.filter(client__business__client__in=business_clients).distinct()
        return {'services_list': services_list}


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
