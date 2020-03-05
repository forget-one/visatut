from django.contrib import admin
from .models import *
# Register your models here.
class FieldInline(admin.StackedInline):
    model = Field
    extra = 0

class AdminCategoryCountry(admin.ModelAdmin):
    exclude = ['']

class AdminField(admin.ModelAdmin):
    exclude = ['']

class AdminCountry(admin.ModelAdmin):
    exclude = ['']

class AdminStaticService(admin.ModelAdmin):
    exclude = ['']

class AdminCountryServices(admin.ModelAdmin):
    exclude = ['']
    inlines = [FieldInline]


admin.site.register(CategoryCountry, AdminCategoryCountry)
admin.site.register(Field, AdminField)
admin.site.register(Country, AdminCountry)
admin.site.register(StaticService, AdminStaticService)
admin.site.register(CountryServices, AdminCountryServices)


class CategoryServicesAdmin(admin.ModelAdmin):
    exclude = ['']

admin.site.register(CategoryServices, CategoryServicesAdmin)
