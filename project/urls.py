
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/xz/', blogxz, name='blog_xz'),
    path('franchise/', franchise, name='franchise'),
    path('services/<country>/', services, name='services'),
    path('service/<id>/', service, name='service'),
]
