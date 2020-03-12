from django.shortcuts import render, HttpResponse
from project.service.models import *
from project.blog.models import *
from project.vacancy.models import *
from django.http import request
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Page 


def index(request):
    service_categories  = ServiceCategory.objects.all()
    static_services     = StaticService.objects.all()
    countries           = Country.objects.all()
    
    genders             = Gender.objects.all()
    work_types          = WorkType.objects.all()
    document_types      = DocumetType.objects.all()

    post_categories     = PostCategory.objects.order_by('-updated')[:3]

    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'index.html', locals())



@csrf_exempt
def tell_us(request):
    data = request.POST 
    print(data)
    send_mail(
        f"Sps za babki {data.get('name')}, {data.get('phone')}, {data.get('email')}",
        'you are welcome',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False
)
    return JsonResponse({})

def services(request, country_pk=None, service_category_pk=None):
    if country_pk:
        country             = Country.objects.get(pk=country_pk)
        country_services    = Service.objects.filter(countries__id__in=[country.id,])
    if service_category_pk:
        service_category     = ServiceCategory.objects.get(pk=service_category_pk)
    title = country.title
    return render(request, 'services.html', locals())


# def service(request, id):
#     service   = Service.objects.get(id=id)
#     title     = service.title
#     return render(request, 'service.html', locals())

def service(request, country_pk=None, service_category_pk=None, post_id=None):
    if country_pk:
        country             = Country.objects.get(pk=country_pk)
        country_services    = Service.objects.filter(countries__id__in=[country.id,])
    if service_category_pk:
        service_category     = ServiceCategory.objects.get(pk=service_category_pk)

    service   = Service.objects.get(id=post_id)
    title     = service.title
    return render(request, 'service.html', locals())




def franchise(request):
    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'franchise.html', locals())    
    





def blog(request, slug):
    post_category   = PostCategory.objects.get(slug=slug)
    posts           = Post.objects.filter(post_category=post_category).order_by('-updated')
    paginator       = Paginator(posts, 2)
    page_number     = request.GET.get('page', 1)
    page            = paginator.get_page(page_number)
    is_paginated    = page.has_other_pages()
    prev_url        = ''
    next_url        = ''
    if page.has_previous():
        prev_url = f'{page.previous_page_number()}'

    if page.has_next():
        next_url = f'{page.next_page_number()}'
    title           = post_category.title
    return render(request, 'blog.html', {
        'posts': page.object_list,
        'prev_url': prev_url,
        'next_url': next_url,
        'title': title
        }
    )


def blog_all(request):
    post_categories     = PostCategory.objects.order_by('-updated')
    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'blog_all.html', locals())


def post(request, id):
    post = Post.objects.get(id=id)
    title = post.title
    return render(request, 'post.html', locals())





def partner_europe(request):
    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'partner_europe.html', locals())


def partner_potential(request):
    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'partner_potential.html', locals())


def partner_usa(request):
    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'partner_usa.html', locals())





@csrf_exempt
def search_service(request):
    data = request.POST or request.GET
    print(data)
    print(request.POST.get('vant1'))
    print(request.POST.get('vant2'))
    print(request.POST.get('vant3'))
    print(request.POST.get('vant4'))
    vacancies = Vacancy.objects.filter(
        country__title=request.POST.get('vant1'),
        gender__human_type=request.POST.get('vant2'),
        document__doc_type=request.POST.get('vant4'),
    )
    print(vacancies)
    page, created = Page.objects.get_or_create(
        code    = f"{request.META.get('PATH_INFO')}")
    return render(request, 'search_service.html', locals())







