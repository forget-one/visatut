
from django.urls import path
from .views import *
from .api.tell_us import tell_us
from .api.search import search_service

urlpatterns = [
    path('',                   index,             name='index'),
    path('services/<country_pk>/',    services,   name='services'),
    path('service/<country_pk>/<service_category_pk>/<post_id>/',   service,      name='service'),
    path('blog/<slug>/',       blog,              name='blog'),
    path('post/<slug>/<id>/',  post,              name='post'),
    path('blog_all/',          blog_all,          name='blog_all'),
    path('franchise/',         Franchise.as_view(),        name='franchise'),
    path('partner_europe/',    PartnerEurope.as_view(),    name='partner_europe'),
    path('partner_potential/', PartnerPotential.as_view(), name='partner_potential'),
    path('partner_usa/',       PartnerUsa.as_view(),       name='partner_usa'),
    path('search_service/',    search_service,    name='search_service'),
    path('tell_us/',           tell_us,           name='tell_us'),
]



