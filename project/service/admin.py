from django.contrib import admin
from .models import *


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ] 
    list_display_links = [
        'id',
        'title',
    ]

class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
    list_display_links = [
        'id',
        'title',
    ]

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ] 
    list_display_links = [
        'id',
        'title',
    ]
class StaticServiceAdmin(admin.ModelAdmin):
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


