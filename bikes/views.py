from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from bikes.forms import ClientForm, BikeForm, ServiceForm
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


def add_client(request):
    login_user = request.user
    business = login_user.employee_of.business
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.business = business
            new_client.save()
            return redirect('bikes:client_detail', new_client.id)
    else:
        form = ClientForm()
    return render(request, 'form.html', {'form': form})


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'phone', 'description']
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('bikes:client_detail', args=[self.object.pk])


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


def bike_extra_view(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    services = Service.objects.filter(bike=bike)
    return render(request, 'bike_detail.html', {'bike': bike, 'services': services})


def add_bike(request, pk):
    login_user = request.user
    owner = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            new_bike = form.save(commit=False)
            new_bike.owner = owner
            new_bike.save()
            return redirect('bikes:bike_detail', new_bike.id)
    else:
        form = BikeForm()
    return render(request, 'form.html', {'form': form})


class BikeUpdateView(UpdateView):
    model = Bike
    fields = ['mark', 'model', 'year', 'description']
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('bikes:bike_detail', args=[self.object.pk])


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


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['end', 'price', 'description']
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('bikes:service_detail', args=[self.object.pk])


def add_service(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    owner = Client.objects.get(pk=bike.owner.id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            new_service = form.save(commit=False)
            new_service.client = owner
            new_service.bike = bike
            new_service.save()
            return redirect('bikes:service_detail', new_service.id)
    else:
        form = ServiceForm()
    return render(request, 'form.html', {'form': form})
