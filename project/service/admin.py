from django.contrib import admin
from .models import *
from project.mixins import ViewImageMixin, meta_data

class ServiceCategoryAdmin(ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                ('image', 'view_image'),
            ],
            'classes': 'wide'
        }),
    ] + meta_data
    readonly_fields = ['view_image']
    list_display = ['id', 'title', 'view_image']
    list_display_links = ['id', 'title',]

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.pk == 1 or obj.pk == 2 or obj.pk == 3:
                return False
        return True

class CountryAdmin(ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                ('image', 'view_image'),
                'categories',
            ],
            'classes': 'wide'
        }),
    ] + meta_data
    filter_horizontal = ['categories']
    readonly_fields = ['view_image']
    list_display = ['id', 'title', 'view_image']
    list_display_links = ['id', 'title',]

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'header',
                'countries',
            ],
            'classes': 'wide'
        }),
        ('Переваги, процедура, додатково', {
            'fields': [
                'advantages',
                'procedure',
                'addition',
            ],
        }),
    ] + meta_data
    list_filter = ['countries']
    list_display = [ 'id', 'title',] 
    list_display_links = [ 'id', 'title',]


class StaticServiceAdmin(ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                ('image', 'view_image'),
                'text',
            ],
            'classes': 'wide'
        }),
    ]
    readonly_fields = ['view_image']
    list_display = ['id', 'title', 'view_image']
    list_display_links = ['id', 'title',]



admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(StaticService, StaticServiceAdmin)
