from django.shortcuts import render
from services.models import *
# Create your views here.


def index(request):
    category_country    = CategoryCountry.objects.all()
    countries           = Country.objects.all()
    categoryservices    = CategoryServices.objects.all()
    # countries           = category_country.country
    return render(request, 'index.html', locals())

    
def blog(request):
    return render(request, 'blog.html')


def blogxz(request):
    return render(request, 'blogxz.html')


def franchise(request):
    return render(request, 'franchise.html')


def services(request, country):
    country_services = CountryServices.objects.filter(country__name=country)
    print(country_services)
    return render(request, 'services.html', locals())


def service(request, id):
    data = CountryServices.objects.get(id=id)
    fields = Field.objects.filter(field=data)
    return render(request, 'service.html', locals())


