from django.contrib import admin
from .models import *
from project.mixins import *


class CountryInline(ViewImageMixin, admin.StackedInline):
    model   = Country
    extra   = 0
    fieldsets = [
        (None, {
            'fields': [
                ('title', 'destiny'),
                ('image', 'view_image'),
            ],
            'classes': 'wide'
        }),
    ] + meta_data

    readonly_fields = ['view_image']


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0
    fieldsets = [
        (None, {
            'fields': [
                ('title', 'destiny'),
                'header',
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

    readonly_fields = ['view_image', 'view_image_a']
    list_display = ['id', 'title', 'view_image_a']
    list_display_links = ['id', 'title', 'view_image_a']
    inlines         = [CountryInline]

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if obj.pk == 1 or obj.pk == 2 or obj.pk == 3:
                return False
        return True


class CountryAdmin(ViewOnSiteMixin, ViewImageMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                ('title', 'destiny'),
                ('image', 'view_image'),
                'category',
            ],
            'classes': 'wide'
        }),
    ] + meta_data

    save_as             = True
    readonly_fields     = ['view_image', 'view_image_a']
    list_display        = ['id', 'title', 'view_image_a', 'on_site']
    list_display_links  = ['id', 'title', 'view_image_a']
    inlines             = [ServiceInline]


class ServiceAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                ('title', 'destiny'),
                'header',
                'country',
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

    save_as             = True
    list_display        = [ 'id', 'title', 'on_site'] 
    list_display_links  = [ 'id', 'title']


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
    readonly_fields     = ['view_image', 'view_image_a']
    list_display        = ['id', 'title', 'view_image_a']
    list_display_links  = ['id', 'title', 'view_image_a']



admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(StaticService, StaticServiceAdmin)
