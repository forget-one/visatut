
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<id>/', post, name='post'),
    path('franchise/', franchise, name='franchise'),
    path('services/<slug>/', services, name='services'),
    path('service/<id>/', service, name='service'),
    path('partner_europe/', partner_europe, name='partner_europe'),
    path('partner_potential/', partner_potential, name='partner_potential'),
    path('partner_usa/', partner_usa, name='partner_usa'),
    path('search_service/', search_service, name='search_service'),
]