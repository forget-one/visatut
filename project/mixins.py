from django.utils.safestring import mark_safe
from .models import Page 
from django.shortcuts import render

class ViewOnSiteMixin(object):
    def on_site(self, obj):
        return mark_safe("<a href='%s' target='_blank'>Дивитися на сайті</a>" % obj.get_absolute_url())
    on_site.short_description = "Дивитися на сайті"


class DefaultPageMixin:
    template = None

    def get(self, request):
        page, created = Page.objects.get_or_create(
            slug    = f"{request.build_absolute_uri()}")
        return render(request, self.template, {'page': page})  

class ViewImageMixin(object):
    def view_image(self, obj):
        return mark_safe(f'<a href="{obj.get_image_url()}" target="_blank"><img src="{obj.get_image_url()}" width="100"/></a>')
    view_image.short_description = "Картинка"


meta_data = [
    ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    

