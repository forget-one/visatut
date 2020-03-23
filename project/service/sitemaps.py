from django.contrib.sitemaps import Sitemap 
from .models import Country, Service, ServiceCategory, StaticService


class CountrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'
    i18n = True 

    def items(self):
        return Country.objects.all()
        
    def lastmod(self, obj):
        return obj.updated


class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'
    i18n = True

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated

class ServiceCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'
    i18n = True

    def items(self):
        return ServiceCategory.objects.all()

    def lastmod(self, obj):
        return obj.updated

class StaticServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'
    i18n = True

    def items(self):
        return StaticService.objects.all()

    def lastmod(self, obj):
        return obj.updated