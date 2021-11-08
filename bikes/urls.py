from django.urls import path
from bikes import views

app_name= 'bikes'

urlpatterns = [
    path('', views.start, name='start'),

]