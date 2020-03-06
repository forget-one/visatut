from django.shortcuts import render
from project.services.models import *
from project.blog.models import *
# Create your views here.


def index(request):
    category_country    = CategoryCountry.objects.all()
    countries           = Country.objects.all()
    categoryservices    = CategoryServices.objects.all()
    posts               = Post.objects.all()
    # countries           = category_country.country
    return render(request, 'index.html', locals())

    
def blog(request):
    posts               = Post.objects.all()
    return render(request, 'blog.html', locals())


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html')


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


