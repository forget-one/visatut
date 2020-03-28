from django.contrib.sitemaps import Sitemap 
from .models import Country, Service


class CountrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'

    def items(self):
        return Country.objects.all()
        
    def lastmod(self, obj):
        return obj.updated


class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return obj.updated
