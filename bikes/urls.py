from django.urls import path
from bikes.views import start, ClientsListView, BikesListView, \
    ServicesListView, ClientDetailView, BikeDetailView, ServiceDetailView

app_name = 'bikes'

urlpatterns = [
    path('', start, name='start'),
    path('clients', ClientsListView.as_view(), name='clients'),
    path('client/<str:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('bikes', BikesListView.as_view(), name='bikes'),
    path('bike/<str:pk>', BikeDetailView.as_view(), name='bike_detail'),
    path('services', ServicesListView.as_view(), name='services'),
    path('service/<str:pk>', ServiceDetailView.as_view(), name='service_detail'),
]
