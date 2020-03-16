from django.contrib import admin
from .models import *


class ServiceCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                ('thumbnail', 'img_alt'),
            ],
            'classes': 'wide'
        }),
        ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    list_display = [
        'id',
        'title',
    ]
    list_display_links = [
        'id',
        'title',
    ]

class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                ('thumbnail', 'img_alt'),
                'categories',
            ],
            'classes': 'wide'
        }),
        ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    list_display = [
        'id',
        'title',
    ]
    list_display_links = [
        'id',
        'title',
    ]

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                'header',
                ('categories', 'countries'),
            ],
            'classes': 'wide'
        }),
        ('Переваги, процедура, додатково', {
            'fields': [
                'advantages',
                'procedure',
                'addition',
            ],
            'classes': ['collapse']
        }),
        ('Мета-дані', {
            'fields': [
                'meta_title',
                'meta_descr',
                'meta_key',
            ],
            'classes': ['collapse']
        }),
    ]
    list_display = [
        'id',
        'title',
    ] 
    list_display_links = [
        'id',
        'title',
    ]
class StaticServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'title',
                ('thumbnail', 'img_alt'),
                'text',
            ],
            'classes': 'wide'
        }),
    ]
    list_display = [
        'id',
        'title',
    ] 
    list_display_links = [
        'id',
        'title',
    ]

# class ServiceFeatureAdmin(admin.ModelAdmin):
#     pass 

# class ServiceFeatureCategoryAdmin(admin.ModelAdmin):
#     pass 


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(StaticService, StaticServiceAdmin)

# admin.site.register(ServiceFeature, ServiceFeatureAdmin)
# admin.site.register(ServiceFeatureCategory, ServiceFeatureCategoryAdmin)

