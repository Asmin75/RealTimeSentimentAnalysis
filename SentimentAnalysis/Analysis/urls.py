from django.urls import path

from . import views

app_name = 'Analysis'

urlpatterns = [
    path('', views.analyse, name='analyse'),
]