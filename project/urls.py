
from django.urls import path
from .views import *

urlpatterns = [
    path('',                   index,             name='index'),
    path('services/<country_pk>/<service_category_pk>/',     services,          name='services'),
    path('service/<country_pk>/<service_category_pk>/<post_id>/',     service,          name='service'),
    path('blog/<slug>/',       blog,              name='blog'),
    path('post/<id>/',         post,              name='post'),
    path('blog_all/',          blog_all,          name='blog_all'),
    path('franchise/',         franchise,         name='franchise'),
    # path('service/<id>/',      service,           name='service'),
    path('partner_europe/',    partner_europe,    name='partner_europe'),
    path('partner_potential/', partner_potential, name='partner_potential'),
    path('partner_usa/',       partner_usa,       name='partner_usa'),
    path('search_service/',    search_service,    name='search_service'),
    path('tell_us/',           tell_us,           name='tell_us'),
]



