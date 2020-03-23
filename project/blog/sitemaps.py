from django.contrib.sitemaps import Sitemap 
from .models import Post, PostCategory


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'
    i18n = True 

    def items(self):
        return Post.objects.all()
        
    def lastmod(self, obj):
        return obj.updated


class PostCategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'
    i18n = True

    def items(self):
        return PostCategory.objects.all()

    def lastmod(self, obj):
        return obj.updated