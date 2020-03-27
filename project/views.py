from django.shortcuts import render
from project.service.models import *
from project.blog.models import *
from project.vacancy.models import *
from django.core.paginator import Paginator
from django.conf import settings
from django.views.generic import View
from .mixins import DefaultPageMixin
from .models import Page

class Franchise(DefaultPageMixin, View):
    template = 'franchise.html'

class PartnerEurope(DefaultPageMixin, View):
    template = 'partner_europe.html'

class PartnerPotential(DefaultPageMixin, View):
    template = 'partner_potential.html'

class PartnerUsa(DefaultPageMixin, View):
    template = 'partner_usa.html'

def index(request):
    service_categories  = ServiceCategory.objects.all()
    static_services     = StaticService.objects.all()
    genders             = Gender.objects.all()
    work_types          = WorkType.objects.all()
    document_types      = DocumetType.objects.all()
    post_categories     = PostCategory.objects.order_by('-updated')[:3]
    page, created       = Page.objects.get_or_create(slug = f"{request.get_full_path}")
    return render(request, 'index.html', locals())

def services(request, country_pk):
    country             = Country.objects.get(pk=country_pk)
    country_services    = Service.objects.filter(countries__id__in=[country.pk,])
    service_category    = ServiceCategory.objects.get(countries=country)
    return render(request, 'services.html', locals())

def service(request, country_pk, service_category_pk, post_id):
    country             = Country.objects.get(pk=country_pk)
    country_services    = Service.objects.filter(countries__id__in=[country.pk,])
    service_category    = ServiceCategory.objects.get(pk=service_category_pk)
    service             = Service.objects.get(pk=post_id)
    return render(request, 'service.html', locals())
       
def blog(request, slug):
    post_category   = PostCategory.objects.get(slug=slug)
    posts           = Post.objects.filter(post_category=post_category).order_by('-updated')
    paginator       = Paginator(posts, 2)
    page_number     = request.GET.get('page', 1)
    page            = paginator.get_page(page_number)
    is_paginated    = page.has_other_pages()
    if page.has_previous(): prev_url = f'{page.previous_page_number()}'
    if page.has_next():     next_url = f'{page.next_page_number()}'
    return render(request, 'blog.html', locals())

def blog_all(request):
    post_categories = PostCategory.objects.order_by('-updated')
    page, created   = Page.objects.get_or_create(slug = f"{request.build_absolute_uri()}")
    return render(request, 'blog_all.html', locals())

def post(request, slug, id):
    post_category   = PostCategory.objects.get(slug=slug)
    post            = Post.objects.get(pk=id)
    return render(request, 'post.html', locals())
