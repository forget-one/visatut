from django.shortcuts import render, HttpResponse
from project.services.models import *
from project.blog.models import *
from project.vacancy.models import *
from django.http import request
# Create your views here.


def index(request):
    category_country    = CategoryCountry.objects.all()
    countries           = Country.objects.all()
    categoryservices    = CategoryServices.objects.all()
    posts               = Post.objects.all()
    genders             = Gender.objects.all()
    work_types          = WorkType.objects.all()
    document_types      = DocumetType.objects.all()
    return render(request, 'index.html', locals())


def services(request, slug):
    country             = Country.objects.get(slug=slug)
    country_services    = CountryServices.objects.filter(country=country)
    return render(request, 'services.html', locals())


def service(request, id):
    data = CountryServices.objects.get(id=id)
    fields = Field.objects.filter(field=data)
    return render(request, 'service.html', locals())


def franchise(request):
    return render(request, 'franchise.html')    
    

def blog(request):
    posts               = Post.objects.all()
    return render(request, 'blog.html', locals())


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html')


def partner_europe(request):
    return render(request, 'partner_europe.html')


def partner_potential(request):
    return render(request, 'partner_potential.html')


def partner_usa(request):
    return render(request, 'partner_usa.html')



def search_service(request):
    data = request.POST
    print(request.POST.get('vant1'))
    print(request.POST.get('vant2'))
    print(request.POST.get('vant3'))
    print(request.POST.get('vant4'))
    vacancies = Vacancy.objects.filter()
    return render(request, 'search_service.html', locals())






    
