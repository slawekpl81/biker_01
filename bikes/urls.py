from django.urls import path
from bikes.views import start, ClientsListView, BikesListView, \
    ServicesListView, ClientDetailView, BikeDetailView, ServiceDetailView, client_extra_view, \
    add_client, ClientUpdateView, BikeUpdateView, ServiceUpdateView, add_bike, add_service, bike_extra_view

app_name = 'bikes'

urlpatterns = [
    path('', start, name='start'),
    path('clients', ClientsListView.as_view(), name='clients'),
    # path('client/<str:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client/<str:pk>', client_extra_view, name='client_detail'),
    path('add_client/', add_client, name='add_client'),
    path('update_client/<str:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('bikes/', BikesListView.as_view(), name='bikes'),
    path('bike/<str:pk>', bike_extra_view, name='bike_detail'),
    path('update_bike/<str:pk>', BikeUpdateView.as_view(), name='update_bike'),
    path('add_bike/<str:pk>', add_bike, name='add_bike'),
    path('services', ServicesListView.as_view(), name='services'),
    path('service/<str:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('update_service/<str:pk>', ServiceUpdateView.as_view(), name='update_service'),
    path('add_service/<str:pk>', add_service, name='add_service'),
]
